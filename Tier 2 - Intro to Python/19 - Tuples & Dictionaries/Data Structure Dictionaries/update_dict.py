# 1. Create a dictionary with keys: 'Name', 'Age', and 'Subject'.
student = {
    'Name': 'Levin',
    'Age': 15,
    'Subject': 'Math'
}

# 2. Update the student's age to 18.
student['Age'] = 18
print("\nAfter updating age:")
print(student)

# 3. Add a new key-value pair for 'Grade' with a value of 'A'.
student['Grade'] = 'A'
print("\nAfter adding grade:")
print(student)

# 4. Print the updated dictionary.
print("\nFinal student information:")
for key, value in student.items():
    print(f"{key}: {value}")