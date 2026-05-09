# 39 Student Attendance Analysis using Pandas

import pandas as pd

try:
    # Read CSV file
    df = pd.read_csv("attendance.csv")

    print("Attendance Data:\n")
    print(df)

    # Students with attendance below 75%
    low_attendance = df[df["Attendance"] < 75]

    print("\nStudents with Attendance Below 75%:\n")
    print(low_attendance)

except FileNotFoundError:
    print("Error: File not found")

except Exception as e:
    print("Error:", e)