"""

Tutorial 2: List Slicing and Indexing
Understanding list slicing syntax.
Slicing to extract specific portions of a list.
Negative indexing and slicing.
Using slice assignment to modify portions of a list.
Practical examples of list slicing.

"""
# Creating a list
my_list = [1, 2, 3, 4, 5]

# List slicing
print(my_list[1:3])  # Output: [2, 3]

# Negative indexing and slicing
print(my_list[-2:])  # Output: [4, 5]

# Slice assignment
my_list[2:4] = [8, 9]
print(my_list)  # Output: [1, 2, 8, 9, 5]