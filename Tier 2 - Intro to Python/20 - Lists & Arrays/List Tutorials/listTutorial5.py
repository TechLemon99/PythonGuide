"""

Tutorial 5: Working with Nested Lists
Explanation of nested lists and their practical applications.
Accessing elements in nested lists using multiple indices.
Modifying elements in nested lists.
Iterating through nested lists using loops.

"""

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in nested lists
print(nested_list[1][2])  # Output: 6

# Modifying elements in nested lists
nested_list[0][1] = 10
print(nested_list)  # Output: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]