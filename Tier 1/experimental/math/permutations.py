# USE ITERTOOLS FOR AMOUNT OF PERMUTATIONS FOR A WHOLE DATASET
# USE MATH FOR USER INPUT
from itertools import permutations

data = [1, 2, 3]
perm_list = list(permutations(data))
print(perm_list)