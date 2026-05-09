# 32 Voting Eligibility with Exception Handling

try:
    age_input = input("Enter your age: ")

    age = int(age_input)

    if age < 0:
        print("Invalid age: Age cannot be negative")

    elif age >= 18:
        print("Eligible to vote")

    else:
        print("Not eligible to vote")

except ValueError:
    print("Invalid input: Please enter numeric value only")

except Exception as e:
    print("Error:", e)