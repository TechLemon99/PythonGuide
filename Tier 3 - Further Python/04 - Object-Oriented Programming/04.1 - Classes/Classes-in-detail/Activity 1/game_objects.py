# Player's class
class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race
        self.cls = cls        # Store the player's class
        self.atk = atk        # Store the player's attack power (i.e. damage)
        self.health = health  # Store the player's health points

# Weapon's class
class Weapon:
    def __init__(self, name, category, damage):
        self.name = name      # Store the weapon's name
        self.category = category  # Store the weapon category
        self.damage = damage  # Store the weapon's damage

# Enemy's class
class Enemy:
    def __init__(self, name, race, damage, health):
        self.name = name     # Store the enemy's name
        self.race = race     # Store the enemy's race
        self.damage = damage # Store the enemy's damage
        self.health = health # Store the enemy's health