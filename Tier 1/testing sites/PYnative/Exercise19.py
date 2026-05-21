num = int(input("Number > "))
ranger = int(input("Range > "))

print(f"Multiplication table of {num}:")

for index, i in enumerate(range(num, ranger+1, num)):
    print(f"{num} x {index+1} = {i}")