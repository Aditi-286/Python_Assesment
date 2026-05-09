# 21NumPy and Pandas Student Marks Analysis

import numpy as np
import pandas as pd

# Generate NumPy array of student marks
marks = np.array([
    [85, 78, 90],
    [72, 88, 80],
    [95, 92, 89],
    [60, 70, 75],
    [88, 84, 91]
])

# Convert NumPy array into Pandas DataFrame
df = pd.DataFrame(marks, columns=["Math", "Science", "English"])

print("Student Marks DataFrame:\n")
print(df)

# Display highest marks
print("\nHighest Marks in Each Subject:")
print(df.max())

# Display average marks
print("\nAverage Marks in Each Subject:")
print(df.mean())

# Display subject-wise statistics
print("\nSubject-wise Statistics:")
print(df.describe())