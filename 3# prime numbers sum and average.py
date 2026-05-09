# prime numbers sum and average

n = int(input("Enter the value of N: "))

count = 0
num = 2
sum_prime = 0

print("\nFirst", n, "prime numbers are:")

while count < n:

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        sum_prime += num
        count += 1

    num += 1

average = sum_prime / n

print("\n\nSum of prime numbers =", sum_prime)
print("Average of prime numbers =", average)