# 36 ATM PIN Validation with Account Lock System

correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN correct. Access granted.")
        print("Welcome to ATM services!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN")

        if attempts > 0:
            print("Attempts left:", attempts)

if attempts == 0:
    print("\nAccount locked due to 3 incorrect attempts.")