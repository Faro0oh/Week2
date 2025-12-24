from pathlib import Path
import sys



ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data_workflow.quality import (
    assert_unique_key,
    require_columns,
    assert_non_empty,
    assert_in_range,
)
from data_workflow.transforms import (
    dedupe_keep_latest,
    missingness_report,
    normalize_text,
    add_missing_flags,
    enforce_schema,
)

from data_workflow.io import read_orders_csv, write_parquet
from data_workflow.config import make_paths


def main():
    
    path = make_paths(ROOT)
    raw_orders_path = path.raw / "orders.csv" 
    processed_orders_path = path.processed / "orders_clean.parquet"
    missingness_report_path = path.reports /"missingness_orders.csv"

    orders_df = read_orders_csv(raw_orders_path)

  
    require_columns(
        orders_df,
        ["order_id", "user_id", "amount", "quantity", "status"]
    )
    assert_non_empty(orders_df, name="orders")

   
    orders_df = enforce_schema(orders_df)

    miss_df = missingness_report(orders_df)
    missingness_report_path.parent.mkdir(parents=True, exist_ok=True)
    miss_df.to_csv(missingness_report_path)

  
    orders_df["status_clean"] = normalize_text(orders_df["status"])

    orders_df = add_missing_flags(
        orders_df,
        cols=["amount", "quantity"]
    )

    assert_in_range(
        orders_df["amount"],
        lo=0,
        name="amount"
    )
    assert_in_range(
        orders_df["quantity"],
        lo=0,
        name="quantity"
    )

    write_parquet(orders_df, processed_orders_path)

    print(f"Rows written: {len(orders_df)}")
    print(f"Clean data: {processed_orders_path}")
    print(f"Missingness report: {missingness_report_path}")


if __name__ == "__main__":
    main()
