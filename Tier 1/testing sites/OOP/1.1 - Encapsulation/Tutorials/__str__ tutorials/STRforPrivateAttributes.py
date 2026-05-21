class Person:
    def __init__(self, name, age, city):
        self._name = name
        self._age = age
        self._city = city

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, City: {self._city}"

p1 = Person("Alice", 30, "Sydney")
print(p1)   # calls __str__ automatically
print(str(p1))  # explicitly calls __str__