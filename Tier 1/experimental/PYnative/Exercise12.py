num1 = 0
num2 = 1

terms = int(input("No. of terms > "))

for i in range(terms):
    print(num1, end=" ")

    result = num1 + num2
    num1 = num2
    num2 = result