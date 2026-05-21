num = int(input("Num > ")) # let num be 1
ranger = int(input("Range > ")) # let range be 50

for i in range(num, ranger + 1): # for every num between 1-50
    if i > 1: # let i = 5
        for j in range(2, i): # for every number between 2 and 5
            if (i % j) == 0: # if 5/j == 0 (not a prime)
                break # break loop
        else:
            print(i)