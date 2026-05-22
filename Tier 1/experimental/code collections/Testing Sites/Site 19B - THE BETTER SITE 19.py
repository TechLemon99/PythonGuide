subjects = ["English", "Software", "Drama", "Science", "Sport"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def list_subjects():
    for index, subject in enumerate(subjects):
        print("Period", index+1, ":", subject)

def organise():
    print(f"{days[i]}\n")
    list_subjects()
    subjects.append(subjects[0])
    subjects.remove(subjects[0])

print("---------------------")

while True:
        choice = input("Which day do u want > ")

        if choice == "1":
            i = 0
            organise()
            break
        elif choice == "2":
            i = 1
            organise()
            break
        elif choice == "3":
            i = 2
            organise()
            break
        elif choice == "4":
            i = 3
            print(f"{days[i]}\n")
            list_subjects(subjects)
            subjects.append(subjects[0])
            subjects.remove(subjects[0])
            break
        elif choice == "5":
            i = 4
            print(f"{days[i]}\n")
            list_subjects(subjects)
            subjects.append(subjects[0])
            subjects.remove(subjects[0])
            break
        elif choice == "e":
            exit()