"""

Tutorial 4: Every Single List Function Explained
Sorting lists using the sorted() function and the .sort() method.
Custom sorting using the key parameter.
Reversing a list using the reversed() function or the .reverse() method.
Sorting lists in place versus creating a new sorted list.

"""

theory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
extension = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

theory.append(1) # adds item at the end. output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
theory.insert(1, 10) # inserts items at given position. output: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 0]
theory2 = theory.copy() # copies the list
theory.extend(extension) # extends the list by adding elements from another list. output: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
theory.reverse() # reverses list. output: [0, 9, 8, 7, 6, 5, 4, 3, 2, 10, 1]
theory.sort() # sorted in order. output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
theory.count # count how many of a certain number in list. output: 1
theory.index # check for existence of item in list. output: 1
theory.pop # removes last item from list. output: 9
theory.remove # removes items of list. output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
theory.clear # clear whole list
# (x in numbers) - check if this exists

# -----------------------------------------------------------------------------------------------------

from statistics import median

# Create lists
numbers = [10, 5, 8, 2, 7]
numbers2 = [3, 6, 9, 1, 4]
numbers3 = [11, 4, 5, 6, 8]
numbers4 = [1, 3, 4, 6, 7]
numbers5 = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 10]

# These work not only on lists but also on other iterable objects such as sets and tuples
print(len(numbers), "Len") # Number of numbers
print(max(numbers), "Max") # Max number
print(min(numbers), "Min") # Min number
print(sum(numbers), "Sum") # Total sum of numbers
print(median(numbers), "Median") # Median of numbers
print(sorted(numbers), "Sorted") # Organize the list
print(list(enumerate(numbers)), "Enumerate") # Show index and value
print(list(reversed(numbers)), "Reversed") # Reverse the list

numbers.reverse() # Reverse the list option 2
print(numbers, "Reversed Option 2")

numbers.extend(numbers2)
numbers.sort()
print(numbers, "Extended and Sorted")

# zip will only pair up to the length of the shorter list (numbers4)
print(list(zip(numbers3, numbers4)), "Zipped")

numbers.insert(3, 99)
print(numbers, "Inserted 99 at Index 3")

numbers.append(100)
print(numbers, "Appended 100 at the end")

numbers.remove(9)
print(numbers, "Removed 9")

numbers.pop()
numbers.pop(2)
print(numbers, "Popped Index 2 and the last Index")

print(numbers.index(99), "Returns index of the value 99")

print(numbers5.count(6), "Returns count of the value 6")

copied_list = numbers.copy()
print(copied_list, "Copied List")

numbers.clear()
print(numbers, "Cleared all elements")