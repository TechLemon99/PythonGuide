# 1. Define a Class
class Dog:
    # The __init__ method is a constructor, called when a new object is created.
    # 'self' refers to the instance of the class itself.
    def __init__(self, name, breed, age):
        self.name = name  # Attribute: name of the dog
        self.breed = breed  # Attribute: breed of the dog
        self.age = age  # Attribute: age of the dog

    # A method (function defined within a class)
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Create Objects (Instances) of the Class
# dog1 and dog2 are objects of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Lucy", "Beagle", 5)

# 3. Access Attributes and Call Methods of Objects
print(f"{dog1.name} is a {dog1.breed} and is {dog1.age} years old.")
print(dog1.bark())

print(f"{dog2.name} is a {dog2.breed} and is {dog2.age} years old.")
print(dog2.bark())