# TODO: Open "student_data.txt" in read mode
with open("File Handling/student_age.txt", "r") as file:

    # TODO: Create dictionary student_dict 
    student_dict = {}

    # TODO: For each line, split line into name and age (separated by comma)
    for line in file:
        name, age = line.strip().split(',')

        # TODO: Store in the dictionary with the name as the key and age as the value
        student_dict[name] = age

# TODO: Print the dictionary
print(student_dict)