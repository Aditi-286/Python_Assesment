# Set Operations Program

set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

print("\nUnion:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

if set1.issubset(set2):
    print("First set is a subset of second set")
elif set2.issubset(set1):
    print("Second set is a subset of first set")
else:
    print("No set is a subset of the other")