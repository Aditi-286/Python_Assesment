# 26 Separate Vowels and Consonants from a Sentence

sentence = input("Enter a sentence: ").lower()

vowels_list = []
consonants_list = []

vowels = "aeiou"

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowels_list.append(char)
        else:
            consonants_list.append(char)

print("\nVowels List:")
print(vowels_list)

print("\nConsonants List:")
print(consonants_list)