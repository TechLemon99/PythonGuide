class Student:
    # Constructor Method to initialise attributes
    def __init__(self, first_name, surname, dob, gender):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.gender = gender

    def testmethod(self):
        return f"Nothing to see here, {self.first_name}."

class Classroom:
    # Constructor Method (builder)
    def __init__(self, title):
        self.class_title = title
        self.students = []

    # Setter Method (writer)
    def add_student(self, first_name, surname, dob, gender):
        self.students.append(Student(first_name, surname, dob, gender))

    # Getter Method (reader)
    def find_student(self, dob): 
        for student in self.students: 
            if student.dob == dob: 
                return student
        return None

student_1 = Student("John", "Doe", "2000-01-01", "Male")
student_2 = Student("Jane", "Smith", "2001-02-02", "Female")
classroom_1 = Classroom("Math Extension 1")
classroom_2 = Classroom("Ancient History")

classroom_1.add_student("John", "Doe", "2000-01-01", "Male")
print("Success")
print(classroom_1.find_student("2000-01-01").first_name)  # Output: John

student_1.first_name = "Johnny"
print(student_1.first_name)

print(student_2.testmethod())