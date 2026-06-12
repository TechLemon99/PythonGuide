"""

Tutorial 3: List Comprehensions
Introduction to list comprehensions as a concise way to create lists.
Syntax of list comprehensions.
Examples of list comprehensions for creating lists with specific patterns.
Conditional list comprehensions with if statements.
Nested list comprehensions.

"""

# Creating a list
my_list = [1, 2, 3, 4, 5]

odd_numbers = [x for x in my_list if x % 2 == 1]
print(odd_numbers)  # Output: [1, 3, 5]

# Conditional list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]