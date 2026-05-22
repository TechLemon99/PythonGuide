class Animal:
    def __init__(self, name):
        self._name = name  # Protected attribute
    
    def get_sound(self):
        print(f"Sound for {self._name} is undefined")

class Dog(Animal):
    def __init__(self, name, sound):
        """Initialize the Dog with name and sound"""
        super().__init__(name)  # Call parent class constructor
        self._sound = sound     # Protected attribute
    
    def get_sound(self):
        """Override parent method to provide dog-specific sound"""
        super().get_sound()     # Call parent's method first
        print(f"{self._name} the dog says {self._sound}!")

class Cat(Animal):
    def __init__(self, name, sound):
        """Initialize the Cat with name and sound"""
        super().__init__(name)  # Call parent class constructor
        self._sound = sound     # Protected attribute
    
    def get_sound(self):
        """Override parent method to provide cat-specific sound"""
        super().get_sound()     # Call parent's method first
        print(f"{self._name} the cat says {self._sound}!")

# Demonstration of the classes
if __name__ == "__main__":
    # Create instances
    generic_animal = Animal("Animal")
    my_dog = Dog("Doge", "Woof")
    my_cat = Cat("Floppa", "Meow")

    # Test the get_sound() method
    print("--- Animal Sound ---")
    generic_animal.get_sound()

    print("\n--- Dog Sound ---")
    my_dog.get_sound()

    print("\n--- Cat Sound ---")
    my_cat.get_sound()