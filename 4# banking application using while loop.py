# banking application using while loop

balance = 0

while True:

    print("\n----- Banking Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Deposit
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully.")

    # Withdraw
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Check Balance
    elif choice == 3:
        print("Current Balance =", balance)

    # Exit
    elif choice == 4:
        print("Thank you for using the banking application.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")