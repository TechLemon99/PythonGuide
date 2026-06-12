while True:
    try:
        temp = int(input("Temperature: "))
        
        if temp < 0:
            print("FREEZING!")
        elif temp <= 15:
            print("COLD!")
        elif temp <= 25:
            print("MILD!")
        elif temp <= 35:
            print("WARM!")
        elif temp == 67:
            print("SIX SEVEN 👋🤚🖐️✋🖖🫱🫲🫳🫴👌🤏✌️ (u lowk dead if ts real twin 💔🥀)")
        else:
            print("HOT!")
    except ValueError:
        print("sybau twin enter a number it aint that deep 💔🥀")