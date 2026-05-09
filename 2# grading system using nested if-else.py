# grading system using nested if-else

print("Enter marks of five subjects:")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("\nTotal Marks =", total)
print("Percentage =", percentage)

# grade calculation using nested if-else
if percentage >= 90:
    grade = "A+"
    
    if percentage >= 95:
        scholarship = "Eligible for Scholarship"
    else:
        scholarship = "Not Eligible for Scholarship"

else:
    if percentage >= 75:
        grade = "A"
        
        if percentage >= 85:
            scholarship = "Eligible for Scholarship"
        else:
            scholarship = "Not Eligible for Scholarship"

    else:
        if percentage >= 60:
            grade = "B"
            scholarship = "Not Eligible for Scholarship"

        else:
            if percentage >= 40:
                grade = "C"
                scholarship = "Not Eligible for Scholarship"

            else:
                grade = "Fail"
                scholarship = "Not Eligible for Scholarship"

print("Grade =", grade)
print(scholarship)
