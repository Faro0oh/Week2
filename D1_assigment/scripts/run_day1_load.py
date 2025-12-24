from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


sys.path.insert(0, str(ROOT / "src"))


from bootcamp_data.io import read_orders_csv, write_parquet
from bootcamp_data.transforms import enforce_schema
from bootcamp_data.config import make_paths


def main():
    #ETL
    paths = make_paths(ROOT)

    raw_orders_path = paths.raw / "orders.csv"  #Input path
    processed_orders_path = paths.processed / "orders.parquet" #Output path

    
    orders_df = read_orders_csv(raw_orders_path) #Extract

    orders_df = enforce_schema(orders_df) #Transform
    
    write_parquet(orders_df, processed_orders_path)#Load
  
    print(f"Orders rows: {len(orders_df)}") # Print number of rows
    print(f"Written to: {processed_orders_path}") # Print path written to



if __name__ == "__main__":
    main()
