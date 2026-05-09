# Monthly Sales Line Chart Using Matplotlib

import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 45000]

# Create line chart
plt.plot(months, sales, marker='o', label='Sales')

# Add title and labels
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Display chart
plt.show()