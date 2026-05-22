class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}"

p1 = Person("Alice", 30, "Sydney")
print(p1)   # calls __str__ automatically
print(str(p1))  # explicitly calls __str__