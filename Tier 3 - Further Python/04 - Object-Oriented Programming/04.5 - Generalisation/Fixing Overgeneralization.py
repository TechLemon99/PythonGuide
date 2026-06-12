class Person:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Contact: {self.phone}, Email: {self.email}")


class Parent(Person):
    def __init__(self, name, age, phone, email, children):
        super().__init__(name, age, phone, email)
        self.children = children

    def display_details(self):
        super().display_details()
        children_str = ", ".join(self.children)  # Join the list into a string
        print(f"Hello, I am a proud parent living with my beautiful children: {children_str}")


class Student(Person):
    def __init__(self, name, age, phone, email, student_id):
        super().__init__(name, age, phone, email) 
        self.student_id = student_id

    def display_details(self):
        super().display_details()
        print(f"Hello, I am a student. Just in case you want to employ me in the future, my student ID is {self.student_id}. Contact me anytime!")


class Teacher(Person):
    def __init__(self, name, age, phone, email, subject):
        super().__init__(name, age, phone, email)
        self.subject = subject

    def display_details(self):
        super().display_details()
        print(f"Hello, I am a teacher. I teach {self.subject}. Feel free to reach out!")


p = Parent("James", 40, "555-6767", "jimmy575@rizzler.org", ["Kylie", "Chloe"])
p.display_details()

s = Student("Chloe", 16, "555-6969", "queenchloeslayy@rizzler.org", "S12345")
s.display_details()

t = Teacher("Mr G. Thang", 35, "555-9876", "itsyogthang@rizzler.org", "Mathematics")
t.display_details()