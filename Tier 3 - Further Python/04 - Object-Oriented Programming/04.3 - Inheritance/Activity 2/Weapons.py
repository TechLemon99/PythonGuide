class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage
    
    def get_stats(self):
        print(f"Weapon: {self.name}")
        print(f"Category: {self.category}")
        print(f"Damage: {self.damage}")
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_category(self, new_category):
        self.category = new_category
    
    def set_damage(self, new_damage):
        self.damage = new_damage

class Sword(Weapon):
    def __init__(self, name, damage, damage_category="Slashing"):
        super().__init__(name, "Sword", damage)
        self.damage_category = damage_category
    
    def get_stats(self):
        super().get_stats()
        print(f"Damage Type: {self.damage_category}")
        print(f"Critical Damage: {self.damage * 3}")
    
    def set_damage_category(self, new_category):
        self.damage_category = new_category

class Bow(Weapon):
    def __init__(self, name, damage, damage_category="Piercing"):
        super().__init__(name, "Bow", damage)
        self.damage_category = damage_category
    
    def get_stats(self):
        super().get_stats()
        print(f"Damage Type: {self.damage_category}")
        print(f"Critical Damage: {self.damage * 2}")
    
    def set_damage_category(self, new_category):
        self.damage_category = new_category

class Longbow(Bow):
    def __init__(self, name, damage, bow_range=150):
        super().__init__(name, damage, "Piercing")
        self.bow_range = bow_range
    
    def get_stats(self):
        super().get_stats()
        print(f"Range: {self.bow_range}ft")
    
    def set_range(self, new_range):
        self.bow_range = new_range

class Shortbow(Bow):
    def __init__(self, name, damage, bow_range=80):
        super().__init__(name, damage, "Piercing")
        self.bow_range = bow_range
    
    def get_stats(self):
        super().get_stats()
        print(f"Range: {self.bow_range}ft")
    
    def set_range(self, new_range):
        self.bow_range = new_range