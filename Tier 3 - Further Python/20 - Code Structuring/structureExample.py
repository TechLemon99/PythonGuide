# Import the required module
import math

# Define the function to calculate factorial
def factorial(n):
    """
    This function takes a number as input and returns its factorial
    """
    # Check if the input number is positive
    if n >= 0:
        # Calculate the factorial using the math module's factorial function
        result = math.factorial(n)
        return result
    else:
        # Return an error message if the input is negative
        return "Error: Factorial of negative numbers is not defined"

# Get the input from the user
num = int(input("Enter a positive number: "))

# Call the factorial function and store the result in a variable
result = factorial(num)

# Print the result
print("The factorial of", num, "is", result)
