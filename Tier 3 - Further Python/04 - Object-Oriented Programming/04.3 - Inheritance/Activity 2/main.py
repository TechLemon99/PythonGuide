from Weapons import Weapon, Sword, Bow, Longbow, Shortbow

def create_weapon():
    print("\nCreate a New Weapon")
    print("1. Generic Weapon")
    print("2. Sword")
    print("3. Bow")
    print("4. Longbow")
    print("5. Shortbow")
    choice = input("Select weapon type: ")
    
    name = input("Enter weapon name: ")
    damage = int(input("Enter damage value: "))
    
    if choice == "1":
        category = input("Enter weapon category: ")
        return Weapon(name, category, damage)
    elif choice == "2":
        damage_type = input("Enter damage type (Slashing/Piercing/Bludgeoning): ")
        return Sword(name, damage, damage_type)
    elif choice == "3":
        damage_type = input("Enter damage type (Slashing/Piercing/Bludgeoning): ")
        return Bow(name, damage, damage_type)
    elif choice == "4":
        bow_range = int(input("Enter bow range (ft): "))
        return Longbow(name, damage, bow_range)
    elif choice == "5":
        bow_range = int(input("Enter bow range (ft): "))
        return Shortbow(name, damage, bow_range)
    else:
        print("Invalid choice")
        return None

def main():
    inventory = []
    
    inventory.append(Sword("Default Sword", 15))
    inventory.append(Bow("Default Bow", 10))
    inventory.append(Longbow("Default Longbow", 12))
    inventory.append(Shortbow("Default Shortbow", 8))
    
    while True:
        print("\nWeapon Inventory System")
        print("1. View All Weapons")
        print("2. Add New Weapon")
        print("3. Search Weapons")
        print("4. Exit")
        choice = input("Select option: ")
        
        if choice == "1":
            print("\n--- All Weapons ---")
            for i, weapon in enumerate(inventory, 1):
                print(f"\nWeapon #{i}")
                weapon.get_stats()
        elif choice == "2":
            new_weapon = create_weapon()
            if new_weapon:
                inventory.append(new_weapon)
                print("Weapon added successfully!")
        elif choice == "3":
            search_term = input("Enter weapon name to search: ").lower()
            found = [w for w in inventory if search_term in w.name.lower()]
            if found:
                print("\n--- Search Results ---")
                for weapon in found:
                    weapon.get_stats()
            else:
                print("No weapons found with that name.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()