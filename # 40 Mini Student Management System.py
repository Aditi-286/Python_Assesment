# 40 Mini Student Management System

import pandas as pd

students = {}

# Function to add student
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {"Name": name, "Marks": marks}
        print("Student added successfully")

    except ValueError:
        print("Invalid input! Please enter correct data types")

# Function to update student
def update_student():
    try:
        roll = int(input("Enter Roll Number to update: "))

        if roll in students:
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))

            students[roll] = {"Name": name, "Marks": marks}
            print("Student updated successfully")
        else:
            print("Student not found")

    except ValueError:
        print("Invalid input")

# Function to delete student
def delete_student():
    try:
        roll = int(input("Enter Roll Number to delete: "))

        if roll in students:
            del students[roll]
            print("Student deleted successfully")
        else:
            print("Student not found")

    except ValueError:
        print("Invalid input")

# Function to display report using Pandas
def generate_report():
    if len(students) == 0:
        print("No records found")
        return

    df = pd.DataFrame.from_dict(students, orient="index")
    df.index.name = "Roll No"

    print("\nStudent Report:\n")
    print(df)

    print("\nAverage Marks:", df["Marks"].mean())
    print("Highest Marks:", df["Marks"].max())

# Menu-driven program
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Generate Report")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            generate_report()
        elif choice == 5:
            print("Exiting program")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")