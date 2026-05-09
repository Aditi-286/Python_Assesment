# 27 Identify Students Enrolled in Multiple Courses

# Tuples containing student name and course
data = [
    ("Aditi", "Python"),
    ("Rahul", "Java"),
    ("Aditi", "Data Science"),
    ("Sneha", "Python"),
    ("Rahul", "C++"),
    ("Arjun", "Java"),
    ("Sneha", "Machine Learning")
]

# Convert tuples into a dictionary (student -> set of courses)
student_courses = {}

for name, course in data:
    if name in student_courses:
        student_courses[name].add(course)
    else:
        student_courses[name] = {course}

print("Students with their courses:\n")
for name, courses in student_courses.items():
    print(name, ":", courses)

print("\nStudents enrolled in multiple courses:\n")

for name, courses in student_courses.items():
    if len(courses) > 1:
        print(name, "-", courses)