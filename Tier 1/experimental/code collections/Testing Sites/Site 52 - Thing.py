import os
import time

def clear_console():
    """Clears the console screen."""
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')

adj = ["red", "big", "tasty"] # lists
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

time.sleep(3)
clear_console()

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])  # Output: apple

my_tuple = (10, 20, 30, "orange")
print(my_tuple[1]) # Output: 20
print(my_tuple[3]) # Output: orange

# A list containing an integer, a string, and a float
list2 = [10, "hello", 3.14]
print(list2[0])
print(list2[1])
print(list2[2])

# A tuple containing an integer, a string, and a boolean
tuple2 = (5, "world", True)
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])