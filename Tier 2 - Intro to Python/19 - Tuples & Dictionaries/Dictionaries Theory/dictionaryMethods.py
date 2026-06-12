# This lesson demonstrates some of the common methods and properties of dictionaries in Python

# The keys() method returns a list of all the keys in a dictionary
print(person.keys()) # Output: ['name', 'age', 'city']

# The values() method returns a list of all the values in a dictionary
print(person.values()) # Output: ['John Doe', 31, 'New York']

# The items() method returns a list of all the key-value pairs in a dictionary as tuple
print(person.items()) # Output: [('name', 'John Doe'), ('age', 31), ('city', 'New York')]

# The get() method returns the value associated with a key, or a default value if the key doesn't exist
print(person.get('gender', 'Unknown')) # Output: Unknown

# The clear() method removes all items from a dictionary
person.clear()
print(person) # Output: {}

# The len() function returns the number of items in a dictionary
person = {'name': 'Taylor Jackson', 'age': 30, 'city': 'New York'}
print(len(person)) # Output: 3
