import pandas as pd

def safe_left_join(left, right, on, validate = "many_to_one", suffixes=("_left", "_right")):
    return pd.merge(left, right, how="left", on=on, validate=validate, suffixes=suffixes)