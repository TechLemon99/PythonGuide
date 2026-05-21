num = int(input("Number > "))
ranger = int(input("To what range > "))

print(f"Now calculating all values between {num} to {ranger} with a multiple of {num}")

for i in range(num, ranger+1, num):
    print(i)