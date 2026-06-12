# Open a file
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random1.txt")

# Read a file
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random1.txt", "r")
print(f.read())

# Read parts of a file
print(f.read(10))

# Read lines of a file
print(f.readline())
print(f.readline())

# Write to an existing file
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random2.txt", "a")
f.write(" Now the file has more content!")
f.close()

# Overwrite the original content
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random3.txt", "w")
f.write("Whoops! I have deleted the content! Now you don't know what was previously written here!")

# Create a file
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random4.txt", "x")

# Create a new file if it doesn't exist
f = open("Tier 2/19 - File Handling/demo 1/random files for demo/random4.txt", "w")

# Close a file
f.close()