"""
Pipeline: Bronze → Silver → Gold (DuckLake) → SQLite Data Mart
===============================================================
Usage:
    1. Place lake.zip, schema.sql (or create_schema.py) in the same directory as this script.
    2. pip install polars duckdb
    3. python pipeline.py

The script is idempotent – re-running it will recreate every layer from scratch.
"""

import json
import os
import random
import shutil
import sqlite3
import zipfile
from pathlib import Path

import duckdb
import polars as pl

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR   = Path(__file__).parent
LAKE_ZIP     = SCRIPT_DIR / "lake.zip"
LAKE_DIR     = SCRIPT_DIR / "lake"
BRONZE_ROOT  = LAKE_DIR / "bronze"
SILVER_ROOT  = LAKE_DIR / "silver"
GOLD_ROOT    = LAKE_DIR / "gold"
DUCKLAKE_DB  = GOLD_ROOT / "park.ducklake"
SQLITE_DB    = SCRIPT_DIR / "parks_dw.db"
SCHEMA_SQL   = SCRIPT_DIR / "schema.sql"
CREATE_PY    = SCRIPT_DIR / "create_schema.py"

# Spending-category imputation rules
#   category_id → (min, max) for non-zero value; include_zero=True means
#   50 % chance of 0 vs a uniform draw in [min, max].
IMPUTE_RULES = {
    2: {"include_zero": False, "min": 15, "max": 25},   # always has a value
    3: {"include_zero": True,  "min":  9, "max": 12},   # 0 or 9-12
    4: {"include_zero": True,  "min":  3, "max":  8},   # 0 or 3-8
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def impute_amount(category_id: int) -> float:
    """Return an imputed amount obeying the per-category rules."""
    rule = IMPUTE_RULES[category_id]
    if rule["include_zero"] and random.random() < 0.5:
        return 0.0
    return round(random.uniform(rule["min"], rule["max"]), 2)


def mirror_path(src: Path, src_root: Path, dst_root: Path, new_suffix: str) -> Path:
    """
    Translate a bronze path to the corresponding silver path,
    swapping the file suffix.
    """
    rel = src.relative_to(src_root)
    return (dst_root / rel).with_suffix(new_suffix)


# ---------------------------------------------------------------------------
# STEP 0 – Unzip bronze
# ---------------------------------------------------------------------------

def step0_unzip():
    print("\n[STEP 0] Unzipping lake.zip …")
    if not LAKE_ZIP.exists():
        raise FileNotFoundError(f"lake.zip not found at {LAKE_ZIP}")
    with zipfile.ZipFile(LAKE_ZIP) as zf:
        zf.extractall(SCRIPT_DIR)
    print(f"  Extracted to {LAKE_DIR}")


# ---------------------------------------------------------------------------
# STEP 1 – Bronze → Silver (clean visitor_spending, convert all to parquet)
# ---------------------------------------------------------------------------

def step1_bronze_to_silver():
    print("\n[STEP 1] Bronze → Silver …")

    # Remove & recreate silver so we start clean
    if SILVER_ROOT.exists():
        shutil.rmtree(SILVER_ROOT)

    json_files = list(BRONZE_ROOT.rglob("*.json"))
    if not json_files:
        raise RuntimeError("No JSON files found in bronze. Check that lake.zip extracted correctly.")

    for src in json_files:
        dst = mirror_path(src, BRONZE_ROOT, SILVER_ROOT, ".parquet")
        dst.parent.mkdir(parents=True, exist_ok=True)

        is_visitor_spending = src.parts[-1] == "visitor_spending.json" or \
                              "visitor_spending" in src.parts

        # Read JSON lines into a Polars DataFrame
        df = pl.read_ndjson(src)

        if is_visitor_spending:
            df = _clean_visitor_spending(df, src)

        df.write_parquet(dst)
        print(f"  {src.relative_to(LAKE_DIR)}  →  {dst.relative_to(LAKE_DIR)}")

    print("  Silver layer complete.")


def _clean_visitor_spending(df: pl.DataFrame, src: Path) -> pl.DataFrame:
    """
    Impute null amounts in visitor_spending according to category rules.
    Only category_ids 2, 3, 4 may have nulls.

    Strategy: cast amount to Float64, then for each eligible category_id
    build a boolean mask of null rows and fill them with per-row random
    values using a Python list comprehension (avoids map_elements struct issues).
    """
    null_count = df["amount"].null_count()
    if null_count == 0:
        return df

    print(f"    Cleaning {null_count} null(s) in {src.name} …")

    # Work with Python lists for the imputation pass – simple and reliable
    amounts    = df["amount"].cast(pl.Float64).to_list()
    categories = df["category_id"].to_list()

    fixed = []
    for amt, cat_id in zip(amounts, categories):
        if amt is not None:
            fixed.append(amt)
        elif cat_id in IMPUTE_RULES:
            fixed.append(impute_amount(cat_id))
        else:
            print(f"    WARNING: null amount for unexpected category_id={cat_id}; setting 0")
            fixed.append(0.0)

    df = df.with_columns(pl.Series("amount", fixed, dtype=pl.Float64))
    return df


# ---------------------------------------------------------------------------
# STEP 2 – Silver → Gold (DuckLake)
# ---------------------------------------------------------------------------

def step2_silver_to_gold():
    """
    Create a DuckLake (DuckDB + local catalog) from the silver parquet files.

    DuckLake uses the `ducklake` extension. Each silver table becomes a
    DuckLake-managed table in the catalog. The physical files land under
    gold/park.ducklake.files/park/<table_name>/part-000.parquet
    as described in the assignment.
    """
    print("\n[STEP 2] Silver → Gold (DuckLake) …")

    GOLD_ROOT.mkdir(parents=True, exist_ok=True)

    # Remove old ducklake artefacts so re-runs are clean
    if DUCKLAKE_DB.exists():
        DUCKLAKE_DB.unlink()
    files_dir = GOLD_ROOT / "park.ducklake.files"
    if files_dir.exists():
        shutil.rmtree(files_dir)

    con = duckdb.connect()          # in-memory DuckDB to drive the load

    # Install & load the ducklake extension
    con.execute("INSTALL ducklake;")
    con.execute("LOAD ducklake;")

    # Attach the DuckLake catalog backed by the local SQLite metadata file
    # and configure the data path to match the expected gold layout.
    con.execute(f"""
        ATTACH 'ducklake:{DUCKLAKE_DB}'
        AS park (
            DATA_PATH '{files_dir}/park/'
        );
    """)

    # Discover silver tables – each sub-directory of silver/park is a table
    silver_park = SILVER_ROOT / "park"
    table_dirs  = sorted(p for p in silver_park.iterdir() if p.is_dir())

    for tbl_dir in table_dirs:
        table_name = tbl_dir.name
        # Collect all parquet files for this table (across all dt= partitions)
        parquet_files = sorted(tbl_dir.rglob("*.parquet"))
        if not parquet_files:
            print(f"  Skipping {table_name} – no parquet files found.")
            continue

        # Build a glob pattern that DuckDB can use
        glob = str(tbl_dir / "**" / "*.parquet")

        print(f"  Loading {table_name} …")

        # Create the DuckLake table from the silver parquet files
        con.execute(f"""
            CREATE TABLE park.{table_name} AS
            SELECT * FROM read_parquet('{glob}', hive_partitioning=true);
        """)

        # Verify row count
        n = con.execute(f"SELECT COUNT(*) FROM park.{table_name}").fetchone()[0]
        print(f"    {n:,} rows loaded into park.{table_name}")

    con.close()
    print("  Gold layer (DuckLake) complete.")


# ---------------------------------------------------------------------------
# STEP 3 – Gold → SQLite data mart
# ---------------------------------------------------------------------------

def step3_gold_to_sqlite():
    """
    Populate the SQLite dimensional model (parks_dw.db) from the DuckLake.

    Mapping:
      spending_category_dim  ← gold.spending_categories
      visit_dim              ← gold.visits  JOIN gold.visitors, parks, lodging_types
      daily_spend_category_fact ← gold.visitor_spending
                                  JOIN gold.visit_days, visit_dim, spending_category_dim
    """
    print("\n[STEP 3] Gold → SQLite data mart …")

    # ---- 3a. Create the schema ----
    _create_sqlite_schema()

    # ---- 3b. Connect to both databases ----
    con = duckdb.connect()
    con.execute("LOAD ducklake;")
    con.execute(f"ATTACH 'ducklake:{DUCKLAKE_DB}' AS park (READ_ONLY);")

    sqlite_con = sqlite3.connect(SQLITE_DB)
    sqlite_con.execute("PRAGMA foreign_keys = OFF;")   # speed during bulk load

    # ---- 3c. spending_category_dim ----
    print("  Populating spending_category_dim …")
    cats = con.execute("""
        SELECT spending_category_id, category_name
        FROM park.spending_categories
        ORDER BY spending_category_id
    """).fetchall()

    sqlite_con.executemany("""
        INSERT OR IGNORE INTO spending_category_dim (spending_category_id, category_name)
        VALUES (?, ?)
    """, cats)
    sqlite_con.commit()
    print(f"    {len(cats)} rows")

    # Build lookup: spending_category_id → spending_category_key
    cat_key = {
        row[0]: row[1]
        for row in sqlite_con.execute(
            "SELECT spending_category_id, spending_category_key FROM spending_category_dim"
        ).fetchall()
    }

    # ---- 3d. visit_dim ----
    print("  Populating visit_dim …")
    # Inspect actual columns to aid debugging
    for tbl in ("visits", "parks", "visitors", "lodging_types"):
        cols = [r[0] for r in con.execute(f"DESCRIBE park.{tbl}").fetchall()]
        print(f"    {tbl} columns: {cols}")

    # day_count computed as (end_date - start_date) + 1
    visits = con.execute("""
        SELECT
            v.visit_id,
            v.park_id,
            p.park_name,
            p.state                                                  AS park_state,
            vis.home_state,
            lt.lodging_name,
            CAST(strftime(v.start_date::DATE, '%Y%m%d') AS INTEGER) AS start_date_key,
            CAST(strftime(v.end_date::DATE,   '%Y%m%d') AS INTEGER) AS end_date_key,
            (v.end_date::DATE - v.start_date::DATE) + 1             AS day_count
        FROM park.visits v
        JOIN park.parks         p   ON p.park_id          = v.park_id
        JOIN park.visitors      vis ON vis.visitor_id     = v.visitor_id
        JOIN park.lodging_types lt  ON lt.lodging_type_id = v.lodging_type_id
        ORDER BY v.visit_id
    """).fetchall()

    sqlite_con.executemany("""
        INSERT OR IGNORE INTO visit_dim
            (visit_id, park_id, park_name, park_state,
             home_state, lodging_name,
             start_date_key_fk, end_date_key_fk, day_count)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, visits)
    sqlite_con.commit()
    print(f"    {len(visits)} rows")

    # Build lookup: visit_id → visit_key
    visit_key = {
        row[0]: row[1]
        for row in sqlite_con.execute(
            "SELECT visit_id, visit_key FROM visit_dim"
        ).fetchall()
    }

    # ---- 3e. daily_spend_category_fact ----
    print("  Populating daily_spend_category_fact …")
    spends = con.execute("""
        SELECT
            vd.visit_id,
            CAST(strftime(vd.visit_date::DATE, '%Y%m%d') AS INTEGER) AS date_key,
            vs.category_id,
            vs.amount
        FROM park.visitor_spending vs
        JOIN park.visit_days vd ON vd.visit_day_id = vs.visit_day_id
        ORDER BY vd.visit_id, date_key, vs.category_id
    """).fetchall()

    fact_rows = []
    for (visit_id, date_key, category_id, amount) in spends:
        vk  = visit_key.get(visit_id)
        ck  = cat_key.get(category_id)
        if vk is None or ck is None:
            print(f"    WARNING: no key for visit_id={visit_id} or category_id={category_id}; skipping")
            continue
        fact_rows.append((vk, date_key, ck, amount))

    sqlite_con.executemany("""
        INSERT OR IGNORE INTO daily_spend_category_fact
            (visit_key_fk, date_key_fk, spending_category_key_fk, amount)
        VALUES (?,?,?,?)
    """, fact_rows)
    sqlite_con.commit()
    print(f"    {len(fact_rows)} rows")

    sqlite_con.execute("PRAGMA foreign_keys = ON;")
    sqlite_con.close()
    con.close()
    print("  SQLite data mart complete.")
    print(f"\n  Database saved to: {SQLITE_DB}")


def _create_sqlite_schema():
    """Run schema.sql (preferred) or create_schema.py to initialise parks_dw.db."""
    if SQLITE_DB.exists():
        SQLITE_DB.unlink()

    if SCHEMA_SQL.exists():
        print(f"  Creating schema from {SCHEMA_SQL.name} …")
        sql_text = SCHEMA_SQL.read_text()
        con = sqlite3.connect(SQLITE_DB)
        con.executescript(sql_text)
        con.commit()
        con.close()
    elif CREATE_PY.exists():
        print(f"  Creating schema via {CREATE_PY.name} …")
        import importlib.util, sys
        spec = importlib.util.spec_from_file_location("create_schema", CREATE_PY)
        mod  = importlib.util.module_from_spec(spec)
        # The script hard-codes "parks_dw.db" so run from the script dir
        orig_dir = os.getcwd()
        os.chdir(SCRIPT_DIR)
        spec.loader.exec_module(mod)
        mod.main()
        os.chdir(orig_dir)
    else:
        raise FileNotFoundError("Neither schema.sql nor create_schema.py found.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    random.seed(42)   # reproducible imputation

    step1_bronze_to_silver()
    step2_silver_to_gold()
    step3_gold_to_sqlite()

    print("\n✅  Pipeline finished successfully.")
    print(f"   SQLite data mart : {SQLITE_DB}")
    print(f"   DuckLake catalog : {DUCKLAKE_DB}")


if __name__ == "__main__":
    main()
