import random

# A perfect deck of 28 cards with the perfect amount of 4 players. 7 for each.
cards = list(range(1, 29))

print(cards)

player_1 = []
player_2 = []
player_3 = []
player_4 = []

for b in range(7):
    if not cards:
        print("Not enough cards to deal 6 to player 1.")
        break
    rand = random.choice(cards)
    player_1.append(rand)
    cards.remove(rand)

for b in range(7):
    if not cards:
        print("Not enough cards to deal 6 to player 2.")
        break
    rand = random.choice(cards)
    player_2.append(rand)
    cards.remove(rand)

for b in range(7):
    if not cards:
        print("Not enough cards to deal 6 to player 3.")
        break
    rand = random.choice(cards)
    player_3.append(rand)
    cards.remove(rand)

for b in range(7):
    if not cards:
        print("Not enough cards to deal 6 to player 4.")
        break
    rand = random.choice(cards)
    player_4.append(rand)
    cards.remove(rand)

print(*player_1)
print(*player_1)
print(*player_1)
print(*player_1)