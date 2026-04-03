# Syntecxhub Data Science Internship — Week 1, Project 2

## Project: Pandas CSV Reader & Basic Analysis

### Overview
This project demonstrates core Pandas skills using a generated sales dataset
covering 20 orders across 4 regions, 3 categories, and 7 months in 2024.

### Requirements covered
1. Read CSV into a DataFrame and inspect structure (head, tail, dtypes, info)
2. Compute summary statistics (mean, median, min, max, count, grouped stats)
3. Filter rows, select columns, and slice subsets
4. Save filtered results to CSV and Excel files

### Files
| File | Description |
|------|-------------|
| `pandas_csv_analysis.py` | Main script |
| `sales_data.csv` | Auto-generated raw dataset |
| `high_value_orders.csv` | Orders above average revenue |
| `electronics_orders.csv` | Electronics category only |
| `q1_2024_orders.xlsx` | Q1 2024 orders |
| `category_summary.xlsx` | One Excel sheet per category |

### Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install pandas openpyxl
python pandas_csv_analysis.py
```

### Tools used
- Python 3.x
- pandas
- openpyxl