# 33 File Copy Program with Word Count

try:
    source_file = input("Enter source file name: ")
    dest_file = input("Enter destination file name: ")

    # Read from source file
    file1 = open(source_file, "r")
    content = file1.read()
    file1.close()

    # Write to destination file
    file2 = open(dest_file, "w")
    file2.write(content)
    file2.close()

    # Count words
    word_count = len(content.split())

    print("\nFile copied successfully!")
    print("Total words copied:", word_count)

except FileNotFoundError:
    print("Error: Source file not found")

except Exception as e:
    print("Error:", e)