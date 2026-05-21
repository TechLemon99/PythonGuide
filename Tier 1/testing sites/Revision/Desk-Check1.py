X = 1
Y = int(input("Enter Y: "))  # Y = 2
while True:  # REPEAT
    Z = Y
    if X < 7:
        X = X + 1
        if X < 8:
            Output = X * Z
    X = X + 1
    if X > 8:  # UNTIL X > 8
        break
    print(X, Y, Z, Output)
print("Done")
print(X, Y, Z, Output)