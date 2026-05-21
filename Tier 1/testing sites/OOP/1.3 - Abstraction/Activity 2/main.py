from weapons import Sword, Bow

def main():
    # Create sword instance
    excalibur = Sword("Default Sword", "Broadsword", 15, "Slashing")
    
    # Create bow instance
    longbow = Bow("Default Bow", "Longbow", 12, "Piercing")
    
    # Test sword methods
    print("Sword Stats:")
    excalibur.get_stats()
    
    print("\nModifying sword...")
    excalibur.set_stats()
    
    print("\nUpdated Sword Stats:")
    excalibur.get_stats()
    
    # Test bow methods
    print("\nBow Stats:")
    longbow.get_stats()
    
    print("\nModifying bow...")
    longbow.set_stats()
    
    print("\nUpdated Bow Stats:")
    longbow.get_stats()

if __name__ == "__main__":
    main()