# This lesson demonstrates the creation and access of dictionaries in Python

# A dictionary is a collection of key-value pairs, where each key is associated with a value.
# The keys in a dictionary must be unique, but the values can be duplicate.

# To create a dictionary, use curly braces {} and separate each key-value pair with a colon :
person = {'name': 'Taylor Swift', 'age': 30, 'city': 'New York'}

# To access the value associated with a key, use square brackets []
print(person['name']) # Output: Taylor Swift

# If you try to access a key that doesn't exist in the dictionary, you'll get a KeyError
# You can use the in operator to check if a key exists in a dictionary
if 'gender' in person:
  print(person['gender'])
else:
  print("Key not found") # Output: Key not found
