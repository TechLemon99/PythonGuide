while True:
    try:
        age = int(input("enter age: "))
        break
    except ValueError:
        print("Invalid Input.")

if age > 13:
    print("You are old!")
else:
    print("you are young!")