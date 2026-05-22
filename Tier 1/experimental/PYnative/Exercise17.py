num = int(input("Number > "))
term = int(input("Term > "))
sum_seq = 0

# run loop n times
for i in range(0, term):
    print(num, end="+")
    sum_seq += num
    # calculate the next term
    num = num * 10 + 2
print("\nSum of above series is:", sum_seq)