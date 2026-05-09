# File Processing Program

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    content = file.read()

    # Count lines
    file.seek(0)
    lines = file.readlines()
    line_count = len(lines)

    # Count words
    word_count = len(content.split())

    # Count characters
    character_count = len(content)

    print("\nTotal Lines:", line_count)
    print("Total Words:", word_count)
    print("Total Characters:", character_count)

    file.close()

except FileNotFoundError:
    print("Error: File not found")

except Exception as e:
    print("Error:", e)