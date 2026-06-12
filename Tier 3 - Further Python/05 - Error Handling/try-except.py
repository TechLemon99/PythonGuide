try:
    egg = int(input("Enter number of eggs > "))

    if egg % 12 == 0:
        print(f"You have {egg//12} dozen eggs")
    elif egg % 12 != 0:
        print(f"You have {egg} eggs")
    else:
        print("Error")
except ValueError:
    print("Please enter a valid number")