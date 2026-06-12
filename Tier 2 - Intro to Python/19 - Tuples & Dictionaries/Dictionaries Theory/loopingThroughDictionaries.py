# This lesson demonstrates how to loop through dictionaries in Python

person = {'name': 'Taylor Swift', 'age': 31, 'city': 'Nashville'}

# You can use the for loop to iterate through the keys in a dictionary
for key in person:
  print(key) # Output: name, age, city

# You can also use the values() method to iterate through the values in a dictionary
for value in person.values():
  print(value) # Output: Taylor Swift, 31, Nashville

# To loop through both the keys and values, you can use the items() method
for key, value in person.items():
  print(key, value) # Output: name Taylor Swift, age 31, city Nashville