# 3. Lists Make a shopping list program.

# Allow the user to:
# Add an item (append)
# Remove an item (remove)
# View the list in order

# Note: This version uses a dictionary to also track the quantity of each item.

# Start with an empty shopping dictionary
shopping_list = {}

running = True

while running:
    action = input("What do you want to do? (add/remove/view/exit) > ").lower()

    if action == "add":
        item = input("What do you want to add? > ").lower()
        amount = int(input(f"How many {item} do you want to add? > "))

        if item in shopping_list:
            shopping_list[item] += amount
            print(f"Updated {item} to {shopping_list[item]}")
        else:
            shopping_list[item] = amount
            print(f"Added {amount} {item}(s) to the list")

    elif action == "remove":
        item = input("What do you want to remove? > ").lower()
        if item in shopping_list:
            amount = int(input(f"How many {item} do you want to remove? > "))
            
            if amount >= shopping_list[item]:
                del shopping_list[item]
                print(f"Removed all {item} from the list")
            else:
                shopping_list[item] -= amount
                print(f"Removed {amount} {item}(s), now {shopping_list[item]} left")
        else:
            print("Item not found in list.")

    elif action == "view":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Shopping List:")
            for item, amount in shopping_list.items():
                print(f"- {item}: {amount}")

    elif action == "exit":
        running = False
        print("Exiting... Goodbye!")

    else:
        print("Invalid action. Please choose add/remove/view/exit.")
