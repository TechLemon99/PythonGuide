# 1. Create a list named 'students' with at least 4 student names.
students = ['Alice', 'Bob', 'Charlie', 'Diana']

# 2. Print the first and last student's name using indexing.
print(f"First student: {students[0]}")  # First item has index 0.
print(f"Last student: {students[-1]}")  # Negative index counts from end.

# 3. Add a new student to the end of the list.
# Use append() to add a new name to the list.
students.append('Ethan')
print("\nAfter adding Ethan:")
print(students)

# 4. Remove the second student from the list.
# Use pop()to delete an element by index.
removed_student = students.pop(1)  # Removes Bob (index 1)
print(f"\nRemoved student: {removed_student}")

# 5. Print the updated list.
print("\nFinal student list:")
print(students)