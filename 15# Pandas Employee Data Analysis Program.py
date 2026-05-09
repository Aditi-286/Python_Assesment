# Pandas Employee Data Analysis Program

import pandas as pd

# Create employee data
data = {
    "Name": ["Aditi", "Rahul", "Sneha", "Arjun", "Priya"],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [45000, 60000, 55000, 70000, 50000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save data to CSV file
df.to_csv("employees.csv", index=False)

# Read data from CSV file
employees = pd.read_csv("employees.csv")

print("Employee Data:\n")
print(employees)

# Department-wise average salary
average_salary = employees.groupby("Department")["Salary"].mean()

print("\nDepartment-wise Average Salary:\n")
print(average_salary)

# Highest salary employee
highest_salary_employee = employees.loc[employees["Salary"].idxmax()]

print("\nHighest Salary Employee:\n")
print(highest_salary_employee)