class Person:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

P1 = Person("Alice")

print("The current name is:", P1.get_name())
new_name = input("What do you want the new name to be > ")

P1.set_name(new_name)
print("The updated name is: ", P1.get_name())