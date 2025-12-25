import pandas as pd

def require_columns(df: pd.DataFrame, cols: list[str]) -> None:
   #Check that all required columns exist
   #Raise AssertionError with clear message if any are missing 
   missing_col = [col for col in cols if col not in df.columns]
   if missing_col:
       assert not missing_col , f"Missing columns: {missing_col}"
   
def assert_non_empty(df: pd.DataFrame, name: str = "df") -> None:   
    #Check that DataFrame has at least one row
     #Raise AssertionError if empty 
      has_one_row = [row for row in df.index if row not in df.index]
      if not has_one_row:
          assert not has_one_row, f"{name} is empty"
      
def assert_unique_key(df: pd.DataFrame, key: str, *, allow_na: bool = False) -> None :
   #Check that a column contains unique values
   #Check for missing values if allow_na=False
   #Raise AssertionError if duplicates or missing values found  
   unique_values = df[key].nunique(dropna=allow_na)   
   if not allow_na and df[key].isna().any():
        assert not df[key].isna().any(), f"Column {key} contains missing values"
   if unique_values != len(df):
      assert unique_values == len(df), f"Column {key} contains duplicate values"
   
def assert_in_range(s: pd.Series, lo=None, hi=None, name: str = "value") -> None:
       #Check that all values are within a range
       #Ignore missing values (only check non-missing)
       #Raise AssertionError if values are outside range
       non_missing = s[s.notna()]

       if lo is not None:
            bad_lo = non_missing < lo
            assert not bad_lo.any(), (
            f"{name} has values below {lo}: "
            f"{non_missing[bad_lo].tolist()}"
        )
       
       if hi is not None:
           bad_hi = non_missing > hi
           assert not bad_hi.any(), (
           f"{name} has values above {hi}: "
           f"{non_missing[bad_hi].tolist()}"
       )
           


