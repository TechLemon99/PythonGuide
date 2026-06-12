choice1 = input("Have you trained your legs? (Y/N) > ").upper()

if choice1 == "Y":
    choice2 = input("Are you injured? (Y/N) > ").upper()
    if choice2 == "Y":
        print("Rest legs.")
    elif choice2 == "N":
        print("Train legs.")
    else:
        print("I don't know what you are talking about.")
elif choice1 == "N":
    choice2 = input("Are you injured? (Y/N) > ").upper()
    if choice2 == "Y":
        print("Rest legs")
    elif choice2 == "N":
        choice3 = input("Are your legs sore? (Y/N) > ").upper()
        if choice3 == "Y":
            print("Rest legs.")
        elif choice3 == "N":
            print("Train legs.")
        else:
            print("I don't know what you are talking about.")
    else:
        print("I don't know what you are talking about.")
else:
    "I don't know what you are talking about."