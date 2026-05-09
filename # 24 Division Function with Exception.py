# 24 Division Function with Exception Handling

def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except ValueError:
        print("Error: Invalid input, please enter numbers only")

    except Exception as e:
        print("Unexpected error:", e)

# Function call
divide_numbers()