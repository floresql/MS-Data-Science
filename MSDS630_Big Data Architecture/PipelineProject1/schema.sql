-- dw_schema_sqlite.sql
PRAGMA foreign_keys = ON;

-- Drop in dependency order
DROP TABLE IF EXISTS daily_spend_category_fact;
DROP TABLE IF EXISTS visit_dim;
DROP TABLE IF EXISTS spending_category_dim;
DROP TABLE IF EXISTS date_dim;

-- -----------------------
-- Dimensions
-- -----------------------

CREATE TABLE date_dim (
    date_key            INTEGER PRIMARY KEY,      -- e.g., 20260201
    full_date           TEXT NOT NULL UNIQUE,     -- 'YYYY-MM-DD'

    weekday             TEXT NOT NULL,
    weekday_short_name  TEXT NOT NULL,
    weekday_num         INTEGER NOT NULL,         -- 1=Mon .. 7=Sun
    day_of_month        INTEGER NOT NULL,
    week_of_year        INTEGER NOT NULL,         -- %W (00-53)

    month_name          TEXT NOT NULL,
    month_name_short    TEXT NOT NULL,
    month_num           INTEGER NOT NULL,

    first_day_of_month  TEXT NOT NULL,
    last_day_of_month   TEXT NOT NULL,

    year                INTEGER NOT NULL,
    season              TEXT NOT NULL,
    seasonal_year       INTEGER NOT NULL
);

CREATE TABLE spending_category_dim (
    spending_category_key INTEGER PRIMARY KEY AUTOINCREMENT,
    spending_category_id  INTEGER NOT NULL UNIQUE,   -- OLTP business key
    category_name         TEXT NOT NULL UNIQUE
);

CREATE TABLE visit_dim (
    visit_key INTEGER PRIMARY KEY AUTOINCREMENT,
    visit_id  INTEGER NOT NULL UNIQUE,   -- OLTP business key

    -- park attributes live here (no separate park_dim)
    park_id    INTEGER NOT NULL,
    park_name  TEXT NOT NULL,
    park_state TEXT NOT NULL,

    home_state    TEXT NOT NULL,
    lodging_name  TEXT NOT NULL,

    start_date_key_fk INTEGER NOT NULL,
    end_date_key_fk   INTEGER NOT NULL,

    day_count INTEGER NOT NULL,

    FOREIGN KEY (start_date_key_fk) REFERENCES date_dim(date_key),
    FOREIGN KEY (end_date_key_fk)   REFERENCES date_dim(date_key)
);

-- -----------------------
-- Fact (daily by visit + date + category)
-- -----------------------

CREATE TABLE daily_spend_category_fact (
    daily_spend_category_fact_key INTEGER PRIMARY KEY AUTOINCREMENT,

    visit_key_fk INTEGER NOT NULL,
    date_key_fk  INTEGER NOT NULL,
    spending_category_key_fk INTEGER NOT NULL,

    amount NUMERIC NOT NULL,

    FOREIGN KEY (visit_key_fk) REFERENCES visit_dim(visit_key),
    FOREIGN KEY (date_key_fk)  REFERENCES date_dim(date_key),
    FOREIGN KEY (spending_category_key_fk) REFERENCES spending_category_dim(spending_category_key),

    UNIQUE (visit_key_fk, date_key_fk, spending_category_key_fk)
);

-- -----------------------
-- Populate date_dim (SQLite recursive CTE)
-- -----------------------

WITH RECURSIVE dates(d) AS (
  SELECT date('2024-01-01')
  UNION ALL
  SELECT date(d, '+1 day')
  FROM dates
  WHERE d < date('2026-12-31')
)
INSERT INTO date_dim (
    date_key,
    full_date,
    weekday,
    weekday_short_name,
    weekday_num,
    day_of_month,
    week_of_year,
    month_name,
    month_name_short,
    month_num,
    first_day_of_month,
    last_day_of_month,
    year,
    season,
    seasonal_year
)
SELECT
    CAST(strftime('%Y%m%d', d) AS INTEGER) AS date_key,
    d AS full_date,

    -- weekday_num: 1=Mon .. 7=Sun
    (((CAST(strftime('%w', d) AS INTEGER) + 6) % 7) + 1) AS weekday_num,

    CASE (((CAST(strftime('%w', d) AS INTEGER) + 6) % 7) + 1)
      WHEN 1 THEN 'Monday'
      WHEN 2 THEN 'Tuesday'
      WHEN 3 THEN 'Wednesday'
      WHEN 4 THEN 'Thursday'
      WHEN 5 THEN 'Friday'
      WHEN 6 THEN 'Saturday'
      ELSE 'Sunday'
    END AS weekday,

    CASE (((CAST(strftime('%w', d) AS INTEGER) + 6) % 7) + 1)
      WHEN 1 THEN 'Mon'
      WHEN 2 THEN 'Tue'
      WHEN 3 THEN 'Wed'
      WHEN 4 THEN 'Thu'
      WHEN 5 THEN 'Fri'
      WHEN 6 THEN 'Sat'
      ELSE 'Sun'
    END AS weekday_short_name,

    CAST(strftime('%d', d) AS INTEGER) AS day_of_month,
    CAST(strftime('%W', d) AS INTEGER) AS week_of_year,

    CAST(strftime('%m', d) AS INTEGER) AS month_num,

    CASE CAST(strftime('%m', d) AS INTEGER)
      WHEN 1 THEN 'January'   WHEN 2 THEN 'February' WHEN 3 THEN 'March'
      WHEN 4 THEN 'April'     WHEN 5 THEN 'May'      WHEN 6 THEN 'June'
      WHEN 7 THEN 'July'      WHEN 8 THEN 'August'   WHEN 9 THEN 'September'
      WHEN 10 THEN 'October'  WHEN 11 THEN 'November' ELSE 'December'
    END AS month_name,

    CASE CAST(strftime('%m', d) AS INTEGER)
      WHEN 1 THEN 'Jan'   WHEN 2 THEN 'Feb' WHEN 3 THEN 'Mar'
      WHEN 4 THEN 'Apr'   WHEN 5 THEN 'May' WHEN 6 THEN 'Jun'
      WHEN 7 THEN 'Jul'   WHEN 8 THEN 'Aug' WHEN 9 THEN 'Sep'
      WHEN 10 THEN 'Oct'  WHEN 11 THEN 'Nov' ELSE 'Dec'
    END AS month_name_short,

    date(d, 'start of month') AS first_day_of_month,
    date(d, 'start of month', '+1 month', '-1 day') AS last_day_of_month,

    CAST(strftime('%Y', d) AS INTEGER) AS year,

    CASE
      WHEN strftime('%m-%d', d) BETWEEN '03-20' AND '06-19' THEN 'Spring'
      WHEN strftime('%m-%d', d) BETWEEN '06-20' AND '09-21' THEN 'Summer'
      WHEN strftime('%m-%d', d) BETWEEN '09-22' AND '12-20' THEN 'Autumn'
      ELSE 'Winter'
    END AS season,

    CASE
      WHEN strftime('%m-%d', d) < '03-20' THEN CAST(strftime('%Y', d) AS INTEGER) - 1
      ELSE CAST(strftime('%Y', d) AS INTEGER)
    END AS seasonal_year
FROM dates
ORDER BY date_key;
