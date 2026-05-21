from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage
    
    @abstractmethod
    def get_stats(self):
        pass
    
    @abstractmethod
    def set_stats(self):
        pass

class Sword(Weapon):
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type
    
    def get_stats(self):
        print(f"Sword: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Melee Type: {self.melee_type}")
    
    def set_stats(self):
        self.name = input("Enter new sword name: ")
        self.category = input("Enter new sword category: ")
        self.damage = int(input("Enter new damage value: "))
        self.melee_type = input("Enter new melee type: ")

class Bow(Weapon):
    def __init__(self, name, category, damage, range_type):
        super().__init__(name, category, damage)
        self.range_type = range_type
    
    def get_stats(self):
        print(f"Bow: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
        print(f"Range Type: {self.range_type}")
    
    def set_stats(self):
        self.name = input("Enter new bow name: ")
        self.category = input("Enter new bow category: ")
        self.damage = int(input("Enter new damage value: "))
        self.range_type = input("Enter new range type: ")