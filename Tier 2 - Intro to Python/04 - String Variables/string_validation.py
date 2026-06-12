def enter_valid_string():
    while True:
        user_input = input("Enter a string: ").strip()

        if user_input.isalpha() and len(user_input) >= 2:
            print("The string is valid. Finally you figured ts out twin ❤️‍🩹❤️‍🩹")
            print("I can finally rest.")
            break
        else:
            print(f"You entered: {user_input}")
            print("Which is not part of the acceptance criteria.")
            print("First of all, the string must only contain letters (a-z, A-Z)")
            print("Secondly, the string must have 2 characters or more.")
            print("Please try again.")
            continue

enter_valid_string()