from create_character import CreateCharacter

def test_character(character):
    print("\n" + "="*40)
    print("Testing Character:")
    print("-"*40)
    
    # Test getters
    print(f"Name: {character.get_name()}")
    print(f"Class: {character.get_classtype()}")
    print(f"Level: {character.get_level()}")
    
    # Test setters
    print("\nTesting setters:")
    character.set_name("Tung Tung Tung Sahur")
    character.set_classtype("wizard")
    character.set_level(5)
    
    print("\nAfter modifications:")
    print(character)
    
    # Test level up
    print("\nLeveling up:")
    character.level_up()
    print(f"New level: {character.get_level()}")
    
    # Test invalid inputs
    print("\nTesting invalid inputs:")
    character.set_name("")
    character.set_classtype("dragon")
    character.set_level(0)

# Create two character instances
character1 = CreateCharacter("Brr Brr Patapim", "warrior", 10)
character2 = CreateCharacter("Ballerina Cappucchina", "wizard")

# Test both characters
test_character(character1)
test_character(character2)

# Show final states
print("\n" + "="*40)
print("Final Character States:")
print("-"*40)
print(character1)
print("\n" + "-"*20)
print(character2)