# Define a function to calculate the area of a circle
def area_of_circle(radius):
    """
    This function calculates the area of a circle, given the radius
    
    Arguments:
    radius: float or int, the radius of the circle
    
    Returns:
    float, the area of the circle
    """
    pi = 3.14 # constant value of pi
    area = pi * (radius ** 2) # formula to calculate the area of a circle
    return area

# Call the function with a radius of 5
result = area_of_circle(5)
print(result)
