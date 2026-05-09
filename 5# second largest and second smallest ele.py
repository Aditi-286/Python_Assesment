# second largest and second smallest element

def find_second(numbers):

    smallest = largest = numbers[0]
    second_smallest = second_largest = numbers[0]

    for num in numbers:

        # finding largest and second largest
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

        # finding smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest, second_largest


# taking input from user
numbers = list(map(int, input("Enter integers separated by space: ").split()))

second_smallest, second_largest = find_second(numbers)

print("Second Smallest Element =", second_smallest)
print("Second Largest Element =", second_largest)