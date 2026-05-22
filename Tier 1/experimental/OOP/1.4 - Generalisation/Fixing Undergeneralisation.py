class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Parent(Person):
    def __init__(self, name, age, phone):
        super().__init__(name, age)  # call Person constructor
        self.phone = phone

    def display_details(self):
        super().display_details()
        print(f"Phone: {self.phone}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_details(self):
        super().display_details()
        print(f"ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_details(self):
        super().display_details()
        print(f"Teaches: {self.subject}")


# Example usage:
p = Parent("Alice", 40, "123-4567")
s = Student("Bob", 16, "S123")
t = Teacher("Carol", 35, "Math")

p.display_details()
print()
s.display_details()
print()
t.display_details()