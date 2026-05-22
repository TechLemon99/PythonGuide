from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random # For random health and damage

# Create an instance of the Player
player_characters = [
    Player('Tralalero Tralala', 'Shark', 'Fighter', 3, 180),
    Player('Bombardino Crocodilo', 'Crocodile', 'Shooter', 4, 150),
    Player('Chimpanzini Bananini', 'Chimpanzee', 'Warrior', 5, 130),
    Player('Lirili Larila', 'Elephant', 'Ranger', 4, 170)
]

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapons = [
    Weapon("Axe of the Seventh Sanctum", 'Axe', random.randint(12, 15)),
    Weapon('Blizzard Striker', 'Sword', random.randint(12, 15)),
    Weapon('HEX Laser Blaster', 'Gun', random.randint(12, 15)),
    Weapon('Ultimate Ban Hammer', 'Hammer', random.randint(12, 15))
]

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy = Enemy(
    "Tung Tung Tung Sahur", 
    "Night Patrol Drum", 
    random.randint(15, 18), 
    random.randint(80, 140)
)

# Select Function
def select_character():
    print("Choose your character:")
    for i, character in enumerate(player_characters, 1):
        print(f"{i}. {character.name} - {character.race} {character.cls} (ATK: {character.atk}, HP: {character.health})")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                selected_player = player_characters[choice-1]
                selected_weapon = weapons[choice-1]
                
                print(f"\nYou have selected {selected_player.name}, the {selected_player.race} {selected_player.cls}!")
                print(f"Your weapon: {selected_weapon.name} ({selected_weapon.category})")
                return selected_player, selected_weapon
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Select character and weapon
player_character, player_weapon = select_character()

# Print the player character details
print("\nPlayer Details:")
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print("\nWeapon Details:")
print(f"Weapon Name: {player_weapon.name}")
print(f"Weapon Category: {player_weapon.category}")
print(f"Weapon Damage: {player_weapon.damage}")

# TODO: Print the enemy character details
print("\nEnemy Details:")
print(f"Enemy Name: {enemy.name}")
print(f"Enemy Race: {enemy.race}")
print(f"Enemy Damage: {enemy.damage}")
print(f"Enemy Health: {enemy.health}")