# Create an ATM program that starts with a balance of ₹10000 and repeatedly displays a menu allowing the user to check balance, 
# deposit money, withdraw money (only if sufficient balance is available), and exit the program.
# ATM Program

balance = 10000

while True:
    print("===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Deposit amount cannot be negative.")
        else:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount < 0:
            print("Withdrawal amount cannot be negative.")
        elif amount <= balance:  
            balance -= amount
            print(f"₹{amount} withdrawn successfully.") 
            print(f"Remaining Balance: ₹{balance}")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")