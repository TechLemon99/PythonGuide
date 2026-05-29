import math

numba = int(input("Enter a numba: "))
base = int(input("Enter base: "))

print(f"{float(math.log(numba, base)):.2g}")