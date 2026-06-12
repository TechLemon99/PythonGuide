#    6. Dictionaries
#    Activity: Build a phone book with a dictionary.
#    Keys = names, Values = phone numbers.
#    Allow the user to:
#    Add a contact
#    Look up a contact
#    Delete a contact
#    Extension: print all contacts sorted alphabetically by name.

# Phone book using a dictionary
phone_book = {}

running = True

while running:
    print("\n--- Phone Book Menu ---")
    print("1. Add a contact")
    print("2. Look up a contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":  # Add contact
        name = input("Enter name: ").title()
        number = input("Enter phone number: ")
        phone_book[name] = number
        print(f"{name} added with number {number}")

    elif choice == "2":  # Look up contact
        name = input("Enter name to look up: ").title()
        if name in phone_book:
            print(f"{name}'s number is {phone_book[name]}")
        else:
            print(f"{name} not found in phone book.")

    elif choice == "3":  # Delete contact
        name = input("Enter name to delete: ").title()
        if name in phone_book:
            del phone_book[name]
            print(f"{name} has been deleted.")
        else:
            print(f"{name} not found.")

    elif choice == "4":  # View all contacts (sorted)
        if phone_book:
            print("\nAll contacts:")
            for name in sorted(phone_book):
                print(f"{name}: {phone_book[name]}")
        else:
            print("Phone book is empty.")

    elif choice == "5":  # Exit
        print("Goodbye!")
        running = False

    else:
        print("Invalid option. Please try again.")