theme = "Light"
volume = 50
username = "Guest"

while True:
    print("\n=== SETTINGS ===")
    print("1. Change Username")
    print("2. Change Theme")
    print("3. Change Volume")
    print("4. View Settings")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        username = input("Enter new username: ")

    elif choice == "2":
        theme = input("Light or Dark? ")

    elif choice == "3":
        volume = int(input("Volume (0-100): "))

    elif choice == "4":
        print("\nCurrent Settings")
        print("Username:", username)
        print("Theme:", theme)
        print("Volume:", volume)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")