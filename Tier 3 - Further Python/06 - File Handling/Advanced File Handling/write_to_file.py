# TODO: Open "movies.txt" in write mode
with open("File Handling/movies.txt", "w") as file:

        # TODO: Ask the user for a favourite movie THREE TIMES. Be efficient in your code.
        for i in range(3):
                movie = input(f"Enter favorite movie #{i+1}: ")

        # TODO: Write the movie to the file with a newline
                file.write(movie + "\n")

# TODO: Let the user know movies have been saved to file
print("\nYour favorite movies have been saved to movies.txt!")

# TODO: Check the file and ensure it worked!
print("\nFile contents:")
with open("File Handling/movies.txt", "r") as file:
    print(file.read())