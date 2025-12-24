import pandas as pd


def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    
   df= df.astype({
       "order_id": "string",
       "user_id": "string",})
   
   df["amount"] = pd.to_numeric(df["amount"], errors='coerce')
   df["quantity"] = pd.to_numeric(df["quantity"], errors='coerce')
      
   
   return df