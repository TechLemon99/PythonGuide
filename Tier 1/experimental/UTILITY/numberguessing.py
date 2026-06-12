import random

print("WELCOME TO GUESS MY NUMBER!")
print("My name is Ray Wing, I am a cl*nker, and you have to guess my number")
print("HERE IS HOW IT WILL WORK! I will think of a random number between 1-100")
print("And all you have to do is guess it!")
print("Fun, right?!")
print("NOW LETS GET TS STARTED")

num = random.randint(1, 100)
already_guessed = []

while True:
    plyr_input = input("Guess a number from 1 - 100: ")
    
    try:
        plyrnum = int(plyr_input)
    except ValueError:
        print("atp js give up gng like tf u saying dawg u delulu")
        continue

    if plyrnum not in range(1, 101):
        print("ts number not within 1-100 gng")
    elif plyrnum != num:
        if plyrnum < num:
            print("ts too low twin lock in")
        else:
            print("why so high gng lock in")
        already_guessed.append(plyrnum)
        print("Already guessed numbers:", already_guessed)
    elif plyrnum == num:
        print("YOU GOT IT BOIIIIIIIIIIIIIIIIIIII TS SO TUFF")
        break
