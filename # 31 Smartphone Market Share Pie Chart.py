# 31 Smartphone Market Share Pie Chart

import matplotlib.pyplot as plt

# Smartphone brands and market share
brands = ["Apple", "Samsung", "Xiaomi", "Realme", "Others"]
market_share = [30, 35, 15, 10, 10]

# Highlight brand with maximum share
explode = [0.1 if share == max(market_share) else 0 for share in market_share]

# Plot pie chart
plt.pie(market_share, labels=brands, autopct="%1.1f%%",
        startangle=140, explode=explode, shadow=True)

# Title
plt.title("Smartphone Market Share")

# Show chart
plt.show()