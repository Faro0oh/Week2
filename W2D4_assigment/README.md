# W2D4 — Exploratory Data Analysis & Visualization

This assignment focuses on performing exploratory data analysis (EDA) and creating publication-ready visualizations using Plotly, as well as applying bootstrap methods for statistical comparison.

## Objectives
- Explore and understand the analytics dataset
- Create reusable visualization helpers
- Generate business insights using data
- Apply bootstrap resampling for statistical inference
- Export charts for reporting

## Project Structure
W2D4_assigment/
- data/processed/analytics_table.parquet
- notebooks/eda.ipynb
- reports/figures/
- src/data_workflow/viz.py
- src/data_workflow/utils.py
- requirements.txt
- README.md

## Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Components
viz.py: bar_sorted, time_line, histogram_chart, save_fig
utils.py: bootstrap_diff_means

## EDA
The notebook loads data, audits it, answers questions with charts, exports figures, and includes a bootstrap comparison.

## Output
Charts in reports/figures and results in the notebook.

## How to Run
jupyter lab
Open notebooks/eda.ipynb and Run All.


