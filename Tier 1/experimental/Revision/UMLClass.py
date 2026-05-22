class Person:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        return f"Full Name: {self.firstName} {self.lastName}"


class Student(Person):
    def __init__(self, firstName: str, lastName: str, studentID: int, homeroom: str):
        super().__init__(firstName, lastName)
        self.studentID = studentID
        self.homeroom = homeroom

    def enrolClass(self, subject):
        subject.studentID.append(self.studentID)
        print(f"{self.printFullName()} has been enrolled into the class {subject.subjectName}.")
        print(f"Student ID: {self.studentID}")
        print(f"Homeroom: {self.homeroom}")


class Parent(Person):
    def __init__(self, firstName: str, lastName: str, occupation: str, alumni: bool):
        super().__init__(firstName, lastName)
        self.occupation = occupation
        self.alumni = alumni


class Subject:
    def __init__(self, subjectName: str):
        self.studentID = []
        self.subjectName = subjectName

    def printStudentList(self):
        print(f"Students enrolled in {self.subjectName}:")
        for id in self.studentID:
            print(f" - Student ID: {id}")


# Create a subject object
subject1 = Subject("Mathematics")

# Create a student and enroll them
student1 = Student("Alice", "Smith", 101, "10A")
student1.enrolClass(subject1)

print()  # Just for spacing

# Create a parent
parent1 = Parent("John", "Smith", "Engineer", True)
print(parent1.printFullName())
print(f"Occupation: {parent1.occupation}")
print(f"Alumni: {parent1.alumni}")

print()  # Just for spacing

# Print the list of students in the subject
subject1.printStudentList()