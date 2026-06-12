# get a string
text = input("Enter a string: ")

# save the string as a txt file
with open('Tier 2/19 - File Handling/demo 2/file.txt', 'w') as f:
    f.write(text)

# open the file in read mode
with open('Tier 2/19 - File Handling/demo 2/file.txt', 'r') as f:
    print(f.read())

# open the file in append mode
with open('Tier 2/19 - File Handling/demo 2/file.txt', 'a') as f:
    f.write(text)