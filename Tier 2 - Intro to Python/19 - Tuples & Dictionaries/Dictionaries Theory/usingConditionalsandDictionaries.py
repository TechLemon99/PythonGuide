# This lesson demonstrates how to use dictionaries with conditional statements in Python

person = {'name': 'Taylor Swift', 'age': 31, 'city': 'Nashville'}

# You can use the in operator to check if a key exists in a dictionary
if 'age' in person:
  print("Key exists") # Output: Key exists
else:
  print("Key not found")

# You can also use the values in a dictionary with conditional statements
if person.get('age') >= 30:
  print("Taylor Swift is 30 or older") # Output: Taylor Swift is 30 or older
else:
  print("Taylor Swift is younger than 30")