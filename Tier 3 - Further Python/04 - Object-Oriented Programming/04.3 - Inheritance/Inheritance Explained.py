# Inheritance allows one class to acquire properties and methods of another.
# We call the base class Parent (Super) and the derived one Child (Sub).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am an animal.")

class Dog(Animal):  # Inherits from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"My name is {self.name}, I am {self.age} years old and I am a {self.breed}.")
        print("Woof! Woof!")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"My name is {self.name}, I am {self.age} years old and I am a {self.breed}.")
        print("Meow! Meow!")

dog = Dog("Buddy", 3, "Golden Retriever")
dog.speak()

cat = Cat("Sir Meows A Lot", 2, "Tabby")
cat.speak()

# Key point: reduces code duplication by reusing parent class code.