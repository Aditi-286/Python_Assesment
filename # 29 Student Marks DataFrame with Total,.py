# 29 Student Marks DataFrame with Total, Percentage and Grades

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Aditi", "Rahul", "Sneha", "Arjun", "Priya"],
    "Math": [85, 72, 95, 60, 88],
    "Science": [78, 88, 92, 70, 84],
    "English": [90, 80, 89, 75, 91]
}

df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculate percentage
df["Percentage"] = df["Total"] / 3

# Assign grades using apply()

def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    else:
        return "C"

df["Grade"] = df["Percentage"].apply(grade)

print(df)