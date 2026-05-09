# 28 Menu-driven Mathematical Utility Program

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n

while True:
    print("\n--- MENU ---")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Armstrong Check")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter number: "))
        print("Factorial:", factorial(num))

    elif choice == 2:
        num = int(input("Enter number: "))
        if is_prime(num):
            print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 3:
        num = int(input("Enter number: "))
        if is_armstrong(num):
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")