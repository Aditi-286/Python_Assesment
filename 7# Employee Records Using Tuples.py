# Employee Records Using Tuples

employees = [
    (101, "Aditi", 45000),
    (102, "Rahul", 52000),
    (103, "Sneha", 48000),
    (104, "Arjun", 60000),
    (105, "Priya", 55000)
]

total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / len(employees)

print("Average Salary:", average_salary)

print("\nEmployees whose salary is above average:\n")

for emp in employees:
    if emp[2] > average_salary:
        print("Employee ID:", emp[0])
        print("Name:", emp[1])
        print("Salary:", emp[2])
        print()