from school_system import Teacher, Student, Parent

# Creating instances
teacher = Teacher("Sae Chabashira", "1995-05-20", "Homeroom")
student = Student("Honami Ichinose", "2009-07-20", "2nd Grade of High School")
parent = Parent("LeBron James", "1984-12-30", "Honami Ichinose")

# Displaying details
print(teacher.display_details())
print(student.display_details())
print(parent.display_details())
print("You are my sunshine~ my only sunshine~ 💖")