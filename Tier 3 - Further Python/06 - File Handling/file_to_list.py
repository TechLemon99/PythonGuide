# TODO: Open the file "students.txt" in read mode
with open("File Handling/students.txt", "r") as file:

    # TODO: Read lines from the file and store them in a list
    lines = file.readlines()

# TODO: Remove extra spaces and newlines from each name. Use list comprehension to STRIP whitespace
cleaned_lines = [line.strip() for line in lines]

# TODO: Print the list
print("Original list:")
print(lines)

# TODO: Print the cleaned-up list
print("\nCleaned list:")
print(cleaned_lines)