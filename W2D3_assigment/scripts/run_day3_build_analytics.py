from pathlib import Path
import sys




ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd
from data_workflow.joins import safe_left_join

from data_workflow.quality import (
    require_columns,
    assert_unique_key, 
)
from data_workflow.transforms import (
    parse_datetime,
    add_time_parts,
    winsorize,
    add_outlier_flag,
)

from data_workflow.io import read_orders_csv, write_parquet
from data_workflow.config import make_paths


def main():
    
    path = make_paths(ROOT)

    
   
    orders_df = read_orders_csv(path.raw / "orders.csv")
    users_df = pd.read_csv(path.raw / "users.csv", dtype={"user_id": "string"})


    require_columns(orders_df, ["order_id", "user_id", "amount", "quantity", "status"])
    require_columns(users_df, ["user_id", "country", "signup_date"])
    assert_unique_key(users_df, "user_id")

    orders_df = parse_datetime(orders_df, "created_at")
    orders_df = add_time_parts(orders_df, "created_at")

    joined = safe_left_join(orders_df, users_df, on="user_id")
    assert len(joined) == len(orders_df)

    joined["amount_wins"] = winsorize(joined["amount"])
    joined = add_outlier_flag(joined, "amount")

    write_parquet(joined, path.processed / "analytics_table.parquet")



   


if __name__ == "__main__":
    main()
