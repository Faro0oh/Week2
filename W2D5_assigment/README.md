# Week 2 Day 5 — ETL Pipeline

## Overview
This project builds a small end‑to‑end ETL pipeline that:
- Loads raw CSV data
- Cleans and validates it
- Transforms it into analytics‑ready format
- Saves processed outputs

## Pipeline Steps
1. Load raw data from `data/raw`
2. Apply schema, missingness, datetime and outlier handling
3. Join dimension tables safely
4. Save final dataset to `data/processed`

## Outputs
- `analytics_table.parquet`

## How to Run
```bash
source venv/bin/activate
PYTHONPATH=src python -m data_workflow.etl
```

## Key Findings
- Revenue is concentrated in a small number of users.
- Order amounts are right‑skewed; winsorization stabilizes analysis.
- Some dates fail parsing and are marked as missing.

## Data Quality Caveats
- Some `created_at` values are invalid and coerced to NaT.
- Outliers are capped but still flagged.
- Joins assume `user_id` is unique in users.


## Checklist

- [ ] `etl.py` has complete ETL pipeline
- [ ] `scripts/run_etl.py` runs successfully
- [ ] Creates `data/processed/_run_meta.json`
- [ ] `reports/summary.md` has all required sections

