def power_rule(exponent):
    # f(x) = x^n -> f'(x) = n * x^(n-1)
    new_coefficient = exponent
    new_exponent = exponent - 1
    
    return f"{new_coefficient}x^{new_exponent}"

try:
    num = int(input("Enter a number like a good boy you are: "))
    print(power_rule(num))
except ValueError:
    print("Bad boy! Enter a number!")