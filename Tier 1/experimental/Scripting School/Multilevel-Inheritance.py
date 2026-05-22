class Person:
	def introduce(self):
		print("Hello, I am a person")

class Student(Person):
	def study(self):
		print("I am studying")

class GraduateStudent(Student):
	def research(self):
		print("I am doing research")

Alex = GraduateStudent()
Alex.introduce()
Alex.study()
Alex.research()