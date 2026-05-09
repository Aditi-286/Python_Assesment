# Input two lists
list1 = [10, 15, 20, 30, 45, 60, 75]
list2 = [15, 25, 30, 45, 50, 60, 90]

# Merge the lists
merged_list = list1 + list2

# Remove duplicates using set
unique_list = list(set(merged_list))

# Sort the list in descending order
unique_list.sort(reverse=True)

# Display numbers divisible by both 3 and 5
print("Numbers divisible by both 3 and 5:")

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        print(num)