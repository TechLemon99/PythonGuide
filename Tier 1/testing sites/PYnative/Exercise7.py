num = int(input("Choice > "))
num2 = num # let num and num2 be 5 as example

for i in range(0, num+1): # from 0-5
    for j in range(num2 - i, 0, -1): # from 5-i to 1 decreasing by 1 every time
        print(j, end=" ") # spaces in between
    print() # formatting