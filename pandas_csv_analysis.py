import pandas as pd
import os

# ──────────────────────────────────────────────
# SECTION 1: Generate a realistic sales dataset
# ──────────────────────────────────────────────

# We build the raw data as a list of dicts, then save it as CSV.
# This simulates what you'd get from a real exported sales report.

raw_data = [
    {"order_id": 1001, "date": "2024-01-05", "region": "North", "category": "Electronics", "product": "Laptop",     "units": 3,  "unit_price": 850.00, "discount_pct": 10},
    {"order_id": 1002, "date": "2024-01-12", "region": "South", "category": "Electronics", "product": "Phone",      "units": 5,  "unit_price": 620.00, "discount_pct": 5},
    {"order_id": 1003, "date": "2024-01-18", "region": "East",  "category": "Furniture",   "product": "Chair",      "units": 10, "unit_price": 145.00, "discount_pct": 0},
    {"order_id": 1004, "date": "2024-02-02", "region": "West",  "category": "Furniture",   "product": "Desk",       "units": 4,  "unit_price": 320.00, "discount_pct": 15},
    {"order_id": 1005, "date": "2024-02-14", "region": "North", "category": "Clothing",    "product": "Jacket",     "units": 8,  "unit_price": 95.00,  "discount_pct": 20},
    {"order_id": 1006, "date": "2024-02-20", "region": "South", "category": "Electronics", "product": "Tablet",     "units": 6,  "unit_price": 430.00, "discount_pct": 10},
    {"order_id": 1007, "date": "2024-03-03", "region": "East",  "category": "Clothing",    "product": "Shoes",      "units": 12, "unit_price": 75.00,  "discount_pct": 5},
    {"order_id": 1008, "date": "2024-03-11", "region": "West",  "category": "Electronics", "product": "Monitor",    "units": 2,  "unit_price": 540.00, "discount_pct": 0},
    {"order_id": 1009, "date": "2024-03-22", "region": "North", "category": "Furniture",   "product": "Bookshelf",  "units": 7,  "unit_price": 210.00, "discount_pct": 10},
    {"order_id": 1010, "date": "2024-04-01", "region": "South", "category": "Clothing",    "product": "T-Shirt",    "units": 20, "unit_price": 25.00,  "discount_pct": 0},
    {"order_id": 1011, "date": "2024-04-09", "region": "East",  "category": "Electronics", "product": "Laptop",     "units": 1,  "unit_price": 850.00, "discount_pct": 5},
    {"order_id": 1012, "date": "2024-04-17", "region": "West",  "category": "Furniture",   "product": "Chair",      "units": 6,  "unit_price": 145.00, "discount_pct": 0},
    {"order_id": 1013, "date": "2024-05-05", "region": "North", "category": "Electronics", "product": "Phone",      "units": 4,  "unit_price": 620.00, "discount_pct": 10},
    {"order_id": 1014, "date": "2024-05-13", "region": "South", "category": "Furniture",   "product": "Desk",       "units": 3,  "unit_price": 320.00, "discount_pct": 5},
    {"order_id": 1015, "date": "2024-05-25", "region": "East",  "category": "Clothing",    "product": "Jacket",     "units": 9,  "unit_price": 95.00,  "discount_pct": 15},
    {"order_id": 1016, "date": "2024-06-04", "region": "West",  "category": "Electronics", "product": "Tablet",     "units": 7,  "unit_price": 430.00, "discount_pct": 0},
    {"order_id": 1017, "date": "2024-06-18", "region": "North", "category": "Clothing",    "product": "Shoes",      "units": 15, "unit_price": 75.00,  "discount_pct": 10},
    {"order_id": 1018, "date": "2024-06-27", "region": "South", "category": "Electronics", "product": "Monitor",    "units": 3,  "unit_price": 540.00, "discount_pct": 5},
    {"order_id": 1019, "date": "2024-07-08", "region": "East",  "category": "Furniture",   "product": "Bookshelf",  "units": 5,  "unit_price": 210.00, "discount_pct": 0},
    {"order_id": 1020, "date": "2024-07-19", "region": "West",  "category": "Clothing",    "product": "T-Shirt",    "units": 30, "unit_price": 25.00,  "discount_pct": 20},
]

# Save as CSV so the rest of the script reads it the normal way
csv_path = "sales_data.csv"
pd.DataFrame(raw_data).to_csv(csv_path, index=False)
print("Dataset saved to sales_data.csv\n")


# ──────────────────────────────────────────────────────────
# REQUIREMENT 1: Read CSV into DataFrame, inspect structure
# ──────────────────────────────────────────────────────────

df = pd.read_csv(csv_path)

# parse the date column properly while we're at it
df["date"] = pd.to_datetime(df["date"])

print("=" * 55)
print("REQUIREMENT 1: Loading and Inspecting the Dataset")
print("=" * 55)

print("\nShape (rows, columns):", df.shape)

print("\nFirst 5 rows (head):")
print(df.head())

print("\nLast 5 rows (tail):")
print(df.tail())

print("\nColumn data types:")
print(df.dtypes)

print("\nBasic info (non-null counts + dtypes):")
print(df.info())


# ────────────────────────────────────────────────────
# Add a calculated column before doing stats
# revenue = units * unit_price * (1 - discount / 100)
# ────────────────────────────────────────────────────

df["revenue"] = df["units"] * df["unit_price"] * (1 - df["discount_pct"] / 100)


# ─────────────────────────────────────────────────────
# REQUIREMENT 2: Summary statistics
# ─────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("REQUIREMENT 2: Summary Statistics")
print("=" * 55)

# overall describe() covers mean/std/min/max/quartiles
print("\nOverall numerical summary:")
print(df[["units", "unit_price", "discount_pct", "revenue"]].describe().round(2))

# manual stats on revenue so they're clearly visible
print("\nRevenue stats (manual):")
print(f"  Mean   : ${df['revenue'].mean():.2f}")
print(f"  Median : ${df['revenue'].median():.2f}")
print(f"  Min    : ${df['revenue'].min():.2f}")
print(f"  Max    : ${df['revenue'].max():.2f}")
print(f"  Count  : {df['revenue'].count()} orders")
print(f"  Total  : ${df['revenue'].sum():.2f}")

# grouped mean revenue by category
print("\nAverage revenue per order by category:")
print(df.groupby("category")["revenue"].mean().round(2))

# grouped total revenue by region
print("\nTotal revenue by region:")
print(df.groupby("region")["revenue"].sum().round(2))


# ─────────────────────────────────────────────────────
# REQUIREMENT 3: Filtering, selecting columns, slicing
# ─────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("REQUIREMENT 3: Filtering, Selecting, Slicing")
print("=" * 55)

# -- Filter: orders where revenue is above average
avg_revenue = df["revenue"].mean()
high_value_orders = df[df["revenue"] > avg_revenue]
print(f"\nOrders with revenue above average (${avg_revenue:.2f}):")
print(high_value_orders[["order_id", "product", "region", "revenue"]])

# -- Filter: Electronics category only
electronics = df[df["category"] == "Electronics"]
print("\nElectronics orders only:")
print(electronics[["order_id", "date", "product", "units", "revenue"]])

# -- Filter: orders with a discount applied
discounted = df[df["discount_pct"] > 0]
print(f"\nOrders with a discount ({len(discounted)} orders):")
print(discounted[["order_id", "product", "discount_pct", "revenue"]])

# -- Select specific columns
print("\nSelecting just product, region, and revenue columns:")
print(df[["product", "region", "revenue"]].head(8))

# -- Slice: rows 5 to 9 using iloc
print("\nSlicing rows index 5–9 (iloc):")
print(df.iloc[5:10])

# -- Slice: Q1 orders using date filter (Jan–Mar 2024)
q1 = df[(df["date"] >= "2024-01-01") & (df["date"] <= "2024-03-31")]
print(f"\nQ1 2024 orders ({len(q1)} rows):")
print(q1[["order_id", "date", "product", "revenue"]])


# ─────────────────────────────────────────────────────
# REQUIREMENT 4: Save filtered results to CSV and Excel
# ─────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("REQUIREMENT 4: Saving Filtered Results")
print("=" * 55)

# save high-value orders to CSV
high_value_orders.to_csv("high_value_orders.csv", index=False)
print("Saved: high_value_orders.csv")

# save electronics orders to CSV
electronics.to_csv("electronics_orders.csv", index=False)
print("Saved: electronics_orders.csv")

# save Q1 data to Excel
q1.to_excel("q1_2024_orders.xlsx", index=False)
print("Saved: q1_2024_orders.xlsx")

# save a full summary table to Excel (one sheet per category)
with pd.ExcelWriter("category_summary.xlsx", engine="openpyxl") as writer:
    for category, group in df.groupby("category"):
        group.to_excel(writer, sheet_name=category, index=False)
print("Saved: category_summary.xlsx  (one sheet per category)")

print("\nAll done.")