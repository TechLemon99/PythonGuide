"""

Tutorial 6: List Methods and Operations
Overview of common list methods such as count(), index(), extend(), clear(), and copy().
Concatenating lists using the + operator.
Checking for membership using in and not in.
Checking for equality between lists.
Cloning lists using slicing or the .copy() method.

"""

# Creating a list
my_list = [1, 2, 3, 4, 5, 8, 8]

# List methods
print(my_list.count(8))  # Output: 2
print(my_list.index(5))  # Output: 4

# Concatenating lists
new_list = my_list + [7, 8]
print(new_list)  # Output: [1, 2, 3, 4, 5, 8, 8, 7, 8]

# Checking for membership
print(5 in my_list)  # Output: True

# copying lists
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 10, 8, 9, 5, 6]

# Check if copied list is same as my_list
print(copied_list is my_list)  # Output: False