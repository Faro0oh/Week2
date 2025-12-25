from pathlib import Path
import pandas as pd
import numpy as np

def read_orders_csv(path: Path) -> pd.DataFrame :
  path = Path(path)
  readDf = pd.read_csv(path , dtype={"order_id": "string", "user_id": "string"} ,  
                       na_values=["?" , "NaN" , "n.a" , "N.A"],
                       keep_default_na= True )
  
  return readDf

def write_parquet(df: pd.DataFrame, path: Path) -> pd.DataFrame:
  path = Path(path)
  path.parent.mkdir(parents=True, exist_ok=True)
  writeParquet = df.to_parquet(path , index= False)
  return writeParquet


def read_parquet(path : Path):
  return pd.read_parquet(path)

