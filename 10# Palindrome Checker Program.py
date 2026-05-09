# Palindrome Checker Program

import string

text = input("Enter a string: ")

cleaned_text = ""

for char in text:
    if char.isalnum():
        cleaned_text += char.lower()

if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")