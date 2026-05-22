class Person:
	def __init__(self, name, age):
		self._name = name # private attribute
		self._age = age # private attribute

	# Getter method
	def get_name(self):
		return self._name

	# Setter method
	def set_age(self, age):
		try:
			if age > 0:
				self._age = age
			else:
				raise ValueError("Age must be a positive integer.")
		except ValueError as e:
			print(e)

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing an attribute through a getter method
print(person1.get_name()) # Output: Alice

# Modifying an attribute through a setter method
person1.set_age(35)
person1.set_age(-5) # Will raise an error

print(person1._name, person1._age) # Directly accessing name (not recommended)