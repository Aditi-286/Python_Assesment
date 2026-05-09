# Fibonacci Program with Even Numbers List

def fibonacci(n):
    a = 0
    b = 1
    even_fibonacci = []

    print("Fibonacci Series:")

    while a <= n:
        print(a, end=" ")

        if a % 2 == 0:
            even_fibonacci.append(a)

        c = a + b
        a = b
        b = c

    print("\n\nEven Fibonacci Numbers:")
    print(even_fibonacci)

# Input from user
n = int(input("Enter the value of N: "))

# Function call
fibonacci(n)