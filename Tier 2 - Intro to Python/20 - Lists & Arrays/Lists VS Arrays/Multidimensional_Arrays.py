import numpy as np  # Import NumPy library

# 1. Create a 2D NumPy array named 'matrix' with 3 rows and 3 columns of numbers.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 2. Print the entire second row.
# The second row is at index 1 (remember, indexing starts at 0).
# Output will be [4, 5, 6]
print("\nSecond row:")
print(matrix[1, :])  # or just matrix[1]

# 3. Change the value in the first row, second column.
# The first row is at index 0, second column is at index 1.
matrix[0, 1] = 20
print("\nAfter changing first row, second column to 20:")
print(matrix)

# 4. Add a new row to the matrix.
# Use np.append to add a row to the existing matrix.
# use this code: new_row = np.array([10, 11, 12])
# use this code: matrix = np.append(matrix, [new_row], axis=0)
new_row = np.array([10, 11, 12])
matrix = np.append(matrix, [new_row], axis=0)
print("\nAfter adding new row:")
print(matrix)

# 5. Print the updated matrix.
print("\nFinal updated matrix:")
print(matrix)