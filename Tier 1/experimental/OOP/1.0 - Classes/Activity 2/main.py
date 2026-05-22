from subjects import Subject

def main():
    subjects = []  # List to store all subjects
    
    while True:
        print("\nSubject Management System")
        print("1. Add a new subject")
        print("2. View a subject")
        print("3. View all subjects")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Add a new subject
            print("\nAdd New Subject")
            name = input("Subject name: ")
            year_level = input("Year level: ")
            class_code = input("Class code: ")
            num_students = input("Number of students enrolled: ")
            
            # Create and add the new subject
            new_subject = Subject(name, year_level, class_code, num_students)
            subjects.append(new_subject)
            print(f"\nSuccessfully added {name}!")
            
        elif choice == "2":
            # View a specific subject
            if not subjects:
                print("\nNo subjects available yet!")
                continue
                
            print("\nAvailable Subjects:")
            for idx, subject in enumerate(subjects, 1):
                print(f"{idx}. {subject.name} (Code: {subject.class_code})")
            
            try:
                sub_choice = int(input("\nEnter subject number to view: ")) - 1
                if 0 <= sub_choice < len(subjects):
                    subjects[sub_choice].display_details()
                else:
                    print("Invalid subject number!")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "3":
            # View all subjects
            Subject.display_all(subjects)
            
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()