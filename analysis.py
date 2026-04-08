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

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()

# Plot
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

print("\nINSIGHTS:")
print("- Highest selling product:", sales_by_product.idxmax())
print("- Total revenue:", df["Sales"].sum())

plt.savefig("sales_chart.png")