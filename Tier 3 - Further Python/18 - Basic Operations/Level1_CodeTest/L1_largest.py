# Define a function to find the largest number in a list
def find_largest(lst):
    """
    This function finds the largest number in a list
    
    Arguments:
    lst: list of int or float, the list of numbers to find the largest in
    
    Returns:
    int or float, the largest number in the list
    """
    # Edge case if the list is empty
    if not lst:
        return None
    
    # Set the first number in the list as the largest number
    largest = lst[0]
    
    # Loop through the rest of the list to find the largest number
    for num in lst[1:]:
        if num > largest:
            largest = num
    
    return largest

# Call the function with a list of numbers
result = find_largest([1, 2, 3, 4, 5])
print(result)
