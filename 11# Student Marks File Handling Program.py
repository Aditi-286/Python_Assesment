# Student Marks File Handling Program
file = open("students.txt", "w")

file.write("Aditi 85\n")
file.write("Rahul 72\n")
file.write("Sneha 90\n")
file.write("Arjun 65\n")
file.write("Priya 78\n")

file.close()

# Reading the file
file = open("students.txt", "r")

students = []
total = 0

for line in file:
    name, marks = line.split()
    marks = int(marks)

    students.append((name, marks))
    total += marks

file.close()

# Calculating average marks
average = total / len(students)

# Finding topper
topper = max(students, key=lambda x: x[1])

print("Topper:", topper[0], "-", topper[1])

print("Average Marks:", average)

print("\nStudents Scoring Below Average:")

for student in students:
    if student[1] < average:
        print(student[0], "-", student[1])