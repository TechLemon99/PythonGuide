num = int(input("Number > "))

i = [int(digit) for digit in str(num)]

maximum = max(i)
minimum = min(i)

print(f"Maximum digit is: {maximum}")
print(f"Minimum digit is: {minimum}")