# Factorial of Even Numbers Program

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

def even_factorials(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(factorial(num))

    return result

# Input list
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
output = even_factorials(numbers)

print("Factorials of even numbers:")
print(output)