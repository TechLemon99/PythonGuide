class Person:
    def __init__(self, name):
        self._name = name  # Using a single underscore for convention to indicate a "protected" attribute

    def get_name(self):
        """Getter method to retrieve the person's name."""
        return self._name

    def set_name(self, new_name):
        """Setter method to update the person's name with validation."""
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            print("Invalid name provided. Name must be a non-empty string.")

# Usage
person1 = Person("Alice")
print(f"Person's name: {person1.get_name()}")

# Usage
person2 = Person("Bob")
print(f"Initial name: {person2.get_name()}")
person2.set_name("Charlie")
print(f"Updated name: {person2.get_name()}")
person2.set_name("") # This will trigger the validation message