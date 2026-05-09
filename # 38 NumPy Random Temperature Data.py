# 38 NumPy Random Temperature Data and Histogram Plot

import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data (e.g., 100 values between 10 and 45)
temperatures = np.random.randint(10, 45, 100)

print("Temperature Data:\n", temperatures)

# Plot histogram
plt.hist(temperatures, bins=10, edgecolor="black")

# Title and labels
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# Show plot
plt.grid(True)
plt.show()