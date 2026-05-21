class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display_details(self):
        return f"Name: {self.name}, DOB: {self.dob}"

class Teacher(Person):
    def __init__(self, name, dob, subject):
        super().__init__(name, dob)
        self.subject = subject

    def display_details(self):
        return f"{super().display_details()}, Teaches: {self.subject}"

class Student(Person):
    def __init__(self, name, dob, grade):
        super().__init__(name, dob)
        self.grade = grade

    def display_details(self):
        return f"{super().display_details()}, Grade: {self.grade}"

class Parent(Person):
    def __init__(self, name, dob, child_name):
        super().__init__(name, dob)
        self.child_name = child_name

    def display_details(self):
        return f"{super().display_details()}, Parent of: {self.child_name}"