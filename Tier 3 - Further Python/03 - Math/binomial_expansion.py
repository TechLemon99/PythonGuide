import math

def binomial_expansion(n):
    for k in range(n + 1):
        coeff = math.comb(n, k)
        print(f"Term {k}: {coeff} * x^{n-k} * y^{k}")

# Example: (x + y)^3
binomial_expansion(3)