list = []

running = True

while running:
    choice = input("Hello > ")
    
    if choice == "1":
        object = input("What do u want to add > ")
        list.append(object)
        print(f"{object} added to list")

    if choice == "2":
        object = input("What do u want to remove > ")
        if len(list) == 0:
            print("Can't remove anything when nothing is in there")
        else:
            if object not in list:
                print("Object not found in list")
            else:
                list.remove(object)
                print(f"{object} removed from list")

    if choice == "3":
        if len(list) == 0:
            print("Nothing in list")
        else:
            for i in list:
                print(i)

    if choice == "4":
        print("Goodbye!")
        running = False