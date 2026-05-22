def Monday():
    print("\nEnglish\nSoftware\nDrama\nScience\nSport\n")

def Tuesday():
    print("\nSport\nEnglish\nSoftware\nDrama\nScience\n")

def Wednesday():
    print("\nScience\nSport\nEnglish\nSoftware\nDrama\n")

def Thursday():
    print("\nDrama\nScience\nSport\nEnglish\nSoftware\n")

def Friday():
    print("\nSoftware\nDrama\nScience\nSport\nEnglish")

while True:
    day = input("Which day > ").lower()

    if day == "monday":
        print(f"Timetable for {day}")
        Monday()
    elif day == "tuesday":
        print(f"Timetable for {day}")
        Tuesday()
    elif day == "wednesday":
        print(f"Timetable for {day}")
        Wednesday()
    elif day == "thursday":
        print(f"Timetable for {day}")
        Thursday()
    elif day == "friday":
        print(f"Timetable for {day}")
        Friday()
    elif day == "exit":
        print("Ending program")
        exit()
    else:
        print("Are you stupid")