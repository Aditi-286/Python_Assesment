# Word Frequency Counter Program

text = input("Enter a paragraph:\n")

# Convert text to lowercase and split into words
words = text.lower().split()

frequency = {}

# Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
print(frequency)

# Find most repeated word
most_repeated = max(frequency, key=frequency.get)

print("\nMost Repeated Word:")
print(most_repeated, "-", frequency[most_repeated], "times")