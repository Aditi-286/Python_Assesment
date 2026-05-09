# 37 Recursive vs Iterative Sum of Digits

# Recursive function
def sum_digits_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits_recursive(n // 10)

# Iterative function
def sum_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Input number
num = int(input("Enter a number: "))

# Calculate using both methods
recursive_result = sum_digits_recursive(num)
iterative_result = sum_digits_iterative(num)

print("\nRecursive Result:", recursive_result)
print("Iterative Result:", iterative_result)

# Comparison
if recursive_result == iterative_result:
    print("Both methods give the same result")
else:
    print("Results are different")