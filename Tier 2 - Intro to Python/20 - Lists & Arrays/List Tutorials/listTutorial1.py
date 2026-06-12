"""

Tutorial 1: Introduction to Lists
Explanation of what lists are and why they're useful.
Basic syntax for creating lists.
Accessing elements in a list using indexing.
Modifying elements in a list.
Length of a list using the len() function.
Basic list methods such as append(), insert(), remove(), and pop().
Iterating through a list using loops.

"""

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1

# Modifying elements in a list
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4, 5]

# Length of a list
print(len(my_list))  # Output: 5

# Basic list methods
my_list.append(6)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]

# Iterating through a list
for item in my_list:
    print(item)
