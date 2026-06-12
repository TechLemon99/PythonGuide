while True:
    try:
        age = int(input("enter age: "))
        break
    except ValueError:
        print("Invalid input")

while age < 13:
    print("You are young!")
    while True:
        try:
            age = input(int("pls enter age: "))
            break
        except ValueError:
            print("Invalid input.")

print("Welcome to the application")