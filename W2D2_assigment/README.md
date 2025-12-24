# Day 2 – Data Quality and Cleaning

## Overview
This project implements a data quality and cleaning pipeline using pandas.
It validates raw data early, applies cleaning transformations, and produces clean outputs and reports.

## Functions and Details

### quality.py

#### require_columns(df, cols)
 - Check that all required columns exist
 - Raise AssertionError with clear message if any are missing

#### assert_non_empty(df, name)
   - Check that DataFrame has at least one row
   - Raise AssertionError if empty

#### assert_unique_key(df, key, allow_na=False)
   - Check that a column contains unique values
   - Check for missing values if `allow_na=False`
   - Raise AssertionError if duplicates or missing values found

#### assert_in_range(series, lo, hi, name)
   - Check that all values are within a range
   - Ignore missing values (only check non-missing)
   - Raise AssertionError if values are outside range

### transforms.py

#### missingness_report(df)
   - Count missing values per column
   - Calculate percentage missing
   - Sort by percentage (most missing first)
   - Return DataFrame with columns: `n_missing`, `p_missing`

#### add_missing_flags(df, cols)
   - Add boolean columns indicating missing values
   - Column names: `{col}__isna` (e.g., `amount__isna`)
   - Don't drop rows - just flag them

#### normalize_text(series)
   - Trim whitespace: `.str.strip()`
   - Convert to lowercase: `.str.casefold()`
   - Collapse multiple spaces: `.str.replace()` with regex

#### apply_mapping(series, mapping)
   - Map values using a dictionary
   - Values not in mapping stay unchanged

#### dedupe_keep_latest(df, key_cols, ts_col)
- Sort by timestamp
- Remove duplicates, keeping the latest row
- Reset index

#### enforce_schema(df)
Casts columns to the correct data types.

## How to Run
source venv/bin/activate
pip install pandas pyarrow
python scripts/run_day2_clean.py

## Outputs
- data/processed/orders_clean.parquet
- data/reports/missingness_orders.csv

## Checklist
- [ ] quality.py implemented with all 4 functions
- [ ] transforms.py implemented with all required helpers
- [ ] run_day2_clean.py runs without errors
- [ ] Missingness report generated
- [ ] Clean data written to Parquet


