# Day 3 — Datetimes, Outliers, and Joins

This assignment builds an analytics-ready table by enriching order data with
time features, handling outliers, and safely joining with user data.

---

##  Objectives

- Parse datetime columns and extract time components
- Handle numeric outliers using IQR and winsorization
- Perform safe joins with validation
- Produce a clean analytics table

---

##  Project Structure

W2D3_assigment/
├── data/
│   ├── raw/
│   │   ├── orders.csv
│   │   └── users.csv
│   └── processed/
│       └── analytics_table.parquet
├── scripts/
│   └── run_day3_build_analytics.py
├── src/
│   └── data_workflow/
│       ├── transforms.py
│       ├── joins.py
│       └── quality.py
└── README.md

---

##  Main Steps

1. Load order and user data from CSV files.
2. Validate required columns and uniqueness constraints.
3. Parse and normalize datetime columns.
4. Extract time-based features (year, month, hour, etc.).
5. Safely join orders with users using a validated left join.
6. Handle outliers using winsorization and flag extreme values.
7. Save the analytics table as a Parquet file.

---
## Functions and Details

### transforms.py

#### datetime(df, col, *, utc) 
   - Convert text column to datetime using `pd.to_datetime(..., errors="coerce", utc=utc)`
   - Use `.assign()` to update the column

#### add_time_parts(df, ts_col)
   - Extract: `date`, `year`, `month`, `dow` (day of week), `hour`
   - Use `.dt` accessor (only works on datetime columns!)

#### assert_unique_key(df, key, allow_na=False)
   - Check that a column contains unique values
   - Check for missing values if `allow_na=False`
   - Raise AssertionError if duplicates or missing values found

#### iqr_bounds(s , k: float = 1.5) -> 
   - Calculate Q1, Q3, IQR
   - Return (lower_bound, upper_bound) using IQR method



#### winsorize(s, lo: float = 0.01, hi: float 0.99) 
 - Cap values at percentiles using `.clip()`


#### add_outlier_flag(df, col, *, k: float = 1.5) 
  - Flag outliers without removing them

#### joins.py


#### safe_left_join(left, right, on, validate, suffixes=...)
- Wrapper around `pd.merge()` with `validate` parameter
- Prevents join explosions by checking cardinality

---

## Checklist

- [ ] `transforms.py` has datetime and outlier functions
- [ ] `joins.py` has `safe_left_join` function
- [ ] `scripts/run_day3_build_analytics.py` runs successfully
- [ ] Creates `data/processed/analytics_table.parquet`

---

##  How to Run

From the project root:

source venv/bin/activate
python scripts/run_day3_build_analytics.py

---

##  Output

The final output is saved to:

data/processed/analytics_table.parquet

---

## Notes

- Invalid or missing datetimes are coerced to NaT and reported with a warning.
- Outliers are capped, not removed, to preserve row counts.
- Joins are validated to prevent accidental row duplication.


