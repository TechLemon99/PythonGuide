# Define a function to calculate the factorial of a number
def factorial(n):
    """
    This function calculates the factorial of a number, given n
    
    Arguments:
    n: int, the number to find the factorial of
    
    Returns:
    int, the factorial of n
    """
    # Edge case if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    
    # Calculate the factorial of n
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    return factorial

# Call the function with n = 5
result = factorial(5)
print(result)
