# This lesson demonstrates how to add, update and delete items from dictionaries in Python

# To add an item to a dictionary, use square brackets [] with a new key and assign a value to it
person['gender'] = 'Male'
print(person) # Output: {'name': 'Taylor Swift', 'age': 30, 'city': 'New York', 'gender': 'Male'}

# To update the value associated with a key, simply assign a new value to the key
person['age'] = 31
print(person) # Output: {'name': 'Taylor Swift', 'age': 31, 'city': 'New York', 'gender': 'Male'}

# To delete an item from a dictionary, use the del keyword
del person['gender']
print(person) # Output: {'name': 'Taylor Swift', 'age': 31, 'city': 'New York'}
