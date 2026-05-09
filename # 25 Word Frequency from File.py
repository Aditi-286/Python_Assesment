# 25 Word Frequency from File and Top Words

from collections import Counter

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")
    text = file.read()
    file.close()

    # Convert to lowercase and split into words
    words = text.lower().split()

    # Store frequencies in dictionary using Counter
    freq = Counter(words)

    print("\nWord Frequencies:")
    print(freq)

    # Top 5 most frequent words
    top5 = freq.most_common(5)

    print("\nTop 5 Most Frequent Words:")
    for word, count in top5:
        print(word, ":", count)

except FileNotFoundError:
    print("Error: File not found")

except Exception as e:
    print("Error:", e)