from minio import Minio
from minio.error import S3Error
import pandas as pd
import io

# ==============================
# CONFIG
# ==============================

ENDPOINT = "s3.class-labs.com"
ACCESS_KEY = "gflores001"
SECRET_KEY = "gflores001-2026"
BUCKET_NAME = "u-gflores001"
SHARED_BUCKET = "shared"

RAW_OBJECT = "raw/sales_data.csv"
CLEAN_OBJECT = "clean/sales_data_clean.csv"


# ==============================
# MINIO CLIENT
# ==============================


client = Minio(
    "s3.class-labs.com",
    access_key="gflores001",
    secret_key="gflores001-2026",
    secure=True,
    region="us-east-1"
)


# ==============================
# MAIN PROCESS
# ==============================

def main():
    try:
        response = client.get_object(BUCKET_NAME, RAW_OBJECT)
        data = response.read()
        df = pd.read_csv(io.BytesIO(data))

        df_clean = df.dropna(subset=["amount"])

        df_clean["amount"] = pd.to_numeric(df_clean["amount"])
        df_clean["date"] = pd.to_datetime(df_clean["date"])

        df_clean = df_clean.sort_values("date")

        clean_buffer = io.BytesIO()
        df_clean.to_csv(clean_buffer, index=False)
        clean_buffer.seek(0)

        client.put_object(
            BUCKET_NAME,
            CLEAN_OBJECT,
            clean_buffer,
            length=clean_buffer.getbuffer().nbytes,
            content_type="text/csv",
            metadata={"cleaned": "true"}
        )

        # ==============================
        # AGGREGATIONS
        # ==============================

        # 5.1 Total sales by month (Jan–Dec order)
        df_clean["month"] = df_clean["date"].dt.month
        df_clean["month_name"] = df_clean["date"].dt.month_name()

        monthly_totals = (
            df_clean
            .groupby(["month", "month_name"])["amount"]
            .sum()
            .reset_index()
            .sort_values("month")
        )

        # 5.2 Total sales by category (high → low)
        category_totals = (
            df_clean
            .groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values("amount", ascending=False)
        )

        # 5.3 Write aggregation results to text file
        with open("aggregation_results.txt", "w") as f:
            f.write("Total Sales by Month:\n")
            f.write(monthly_totals.to_string(index=False))
            f.write("\n\nTotal Sales by Category:\n")
            f.write(category_totals.to_string(index=False))

        # 5.4 Add tax column (5%)
        df_clean["tax"] = df_clean["amount"] * 0.05
        df_clean["amount_with_tax"] = df_clean["amount"] + df_clean["tax"]

        df_clean.to_csv("amount_with_tax.csv", index=False)

        # 5.5 Upload both files to shared bucket using your bucket name as prefix

        # Upload aggregation_results.txt
        client.fput_object(
            SHARED_BUCKET,
            "u-gflores001/aggregation_results.txt",
            "aggregation_results.txt"
        )

        # Upload amount_with_tax.csv
        client.fput_object(
            SHARED_BUCKET,
            "u-gflores001/amount_with_tax.csv",
            "amount_with_tax.csv"
        )

        print("Process completed successfully.")

    except S3Error as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()