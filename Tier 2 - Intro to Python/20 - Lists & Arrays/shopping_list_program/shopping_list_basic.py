# 3. Lists Make a shopping list program.
# Start with ["milk", "bread", "eggs"].
# Allow the user to:
# Add an item (append)
# Remove an item (remove)
# View the list in order
# Extension: Ask the user what they want to buy and check if it’s already in the list.

shopping_list = ["milk", "bread", "eggs"]

running = True

while running:
    action = input("What do you want to do? (add/remove/view/exit) > ").lower()

    if action == "add":
        item = input("What do you want to add? > ")
        if item in shopping_list:
            print("Sorry, item already in list.")
        else:
            shopping_list.append(item)
            print(f"{item} added to list")

    elif action == "remove":
        item = input("What do you want to remove? > ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from list")
        else:
            print("Item not found in list.")

    elif action == "view":
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

    elif action == "exit":
        running = False

    else:
        print("Invalid action. Please choose add/remove/view/exit.")
