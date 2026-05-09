# Armstrong Number Checker Program

n = int(input("Enter how many numbers you want to check: "))

for i in range(n):
    number = int(input("\nEnter a number: "))

    temp = number
    digits = len(str(number))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == number:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")