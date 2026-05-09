# character frequency counter

paragraph = input("Enter a paragraph:\n")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in paragraph:

    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

    else:
        special += 1

result = {
    "Lowercase Letters": lowercase,
    "Uppercase Letters": uppercase,
    "Spaces": spaces,
    "Digits": digits,
    "Special Characters": special
}

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

print("\nCharacter Frequency (Descending Order):")

for category, count in sorted_result:
    print(category, ":", count)