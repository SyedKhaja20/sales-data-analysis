import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# Show first rows
print("Data Preview:")
print(df.head())

# Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_by_product)

# Sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)