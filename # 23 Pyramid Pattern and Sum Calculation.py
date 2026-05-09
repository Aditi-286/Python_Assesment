# 23 Pyramid Pattern and Sum Calculation

rows = int(input("Enter number of rows: "))

num = 1
total_sum = 0

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")

    # Print numbers in pyramid
    for j in range(i):
        print(num, end=" ")
        total_sum += num
        num += 1

    print()

print("\nSum of all numbers in the pattern:", total_sum)