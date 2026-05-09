# 22 Pandas Sales Data and Matplotlib Bar Chart

import pandas as pd
import matplotlib.pyplot as plt

# Read sales data from CSV file
df = pd.read_csv("sales.csv")

# Display data
print("Sales Data:\n")
print(df)

# Product-wise total sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct-wise Sales:\n")
print(product_sales)

# Plot bar chart
plt.bar(product_sales.index, product_sales.values, label="Sales")

# Add title and labels
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Show plot
plt.show()