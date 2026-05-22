class Person:
	def __init__(self, name):
		self.name = name

class Student(Person):
	def __init__(self, name, grade):
		super().__init__(name)
		self.grade = grade

student_1 = Student("John", "A+")
print(student_1.name + " has obtained " + student_1.grade + " grades this year.")