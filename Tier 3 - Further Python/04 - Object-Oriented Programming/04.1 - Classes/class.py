# Classes are object constructors or blueprints.

# Creating a basic class
class myclass:
    x = 5

# Creating an object in a class
p1 = myclass()
print(p1.x)

# When creating more complex classes you need to use specialized function commands such as __init__
class Person:
    def __init__(self, height, name, age):
        self.height = height
        self.name = name
        self.age = age

# Creating full blueprinted classes need to define the perameters in the __init__ command
person1 = Person(170,"jim",20)
print(person1.age)
print(person1.height)
print(person1.age)

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class object():
    pass

# Classes can also inherit from other classes
class Student(Person):
    def __init__(self, height, name, age):
        super().__init__( height, name, age)
        self.graduationyear = 2019