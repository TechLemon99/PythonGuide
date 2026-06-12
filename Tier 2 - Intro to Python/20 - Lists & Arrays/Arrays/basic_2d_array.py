import numpy as np

# Create a 1D array
single_dimensional = np.array([1, 2, 3, 4, 5])

# Print the entire array
print("Array:", single_dimensional)

# Access elements by index
print("First element:", single_dimensional[0])
print("Last element:", single_dimensional[-1])

# Basic operations
sum_of_elements = np.sum(single_dimensional)
mean_of_elements = np.mean(single_dimensional)

print("Sum of elements:", sum_of_elements)
print("Mean of elements:", mean_of_elements)