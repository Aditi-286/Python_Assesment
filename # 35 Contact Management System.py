# 35 Contact Management System

contacts = {}

while True:
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added successfully")

    elif choice == "2":
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Name:", name, "Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice")