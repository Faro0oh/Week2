# Day 1 – Data Workflow: Project Setup & Basic I/O

## Overview
This assignment focuses on setting up a professional data workflow project and building a simple end-to-end ETL pipeline.  
The goal is to read raw CSV data, enforce a clean schema, and write processed outputs in Parquet format.

---

## Learning Objectives
By completing this assignment, you will be able to:
- Create a clean and professional data project structure
- Work with CSV input files using pandas
- Handle missing and invalid values safely
- Enforce consistent data schemas
- Write processed data using the Parquet format
- Build a runnable ETL script

---

## Project Structure
The project follows a standard data engineering layout:


---

## Data Description

### Raw Files
- **orders.csv**
  - order_id
  - user_id
  - amount
  - quantity
  - created_at
  - status

- **users.csv**
  - user_id
  - country
  - signup_date

Raw data is stored unchanged in `data/raw/`.

---

## Key Components

### config.py
Defines a frozen `Paths` dataclass that centralizes all project paths.  
This ensures consistent and cross-platform path handling using `pathlib`.

---

### io.py
Provides reusable input/output utilities:
- Reading CSV files with correct data types
- Centralized missing value handling
- Writing processed data in Parquet format

---

### transforms.py
Contains data transformation logic:
- `enforce_schema` converts IDs to string types
- Numeric fields are safely converted using `pd.to_numeric`
- Invalid values are coerced into missing values instead of raising errors

---

### run_day1_load.py
The main ETL script that:
1. Loads raw CSV files
2. Applies schema enforcement
3. Writes processed Parquet outputs
4. Logs row counts and output locations

The script is designed to be reproducible and run end-to-end.

---

## How to Run

Activate the virtual environment:
```bash
source .venv/bin/activate

 Run the ETL script from the project root
 python scripts/run_day1_load.py

 ## output
 data/processed/orders.parquet