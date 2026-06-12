class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_all_in_tuple(self):
        return (self.name, self.age, self.city)
    
    def get_all_as_string(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}"

p1 = Person("Alice", 30, "Sydney")
print(p1.get_all_in_tuple())
print(p1.get_all_as_string())