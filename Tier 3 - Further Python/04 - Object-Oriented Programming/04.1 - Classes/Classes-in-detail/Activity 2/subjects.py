class Subject:
    def __init__(self, name, year_level, class_code, num_students):
        self.name = name
        self.year_level = year_level
        self.class_code = class_code
        self.num_students = num_students
    
    def display_details(self):
        print(f"\nSubject: {self.name}")
        print(f"Year Level: {self.year_level}")
        print(f"Class Code: {self.class_code}")
        print(f"Students Enrolled: {self.num_students}")
    
    @staticmethod
    def display_all(subjects):
        if not subjects:
            print("\nNo subjects available yet!")
            return
        
        print("\nAll Subjects:")
        for idx, subject in enumerate(subjects, 1):
            print(f"\nSubject {idx}:")
            print(f"  Name: {subject.name}")
            print(f"  Year Level: {subject.year_level}")
            print(f"  Class Code: {subject.class_code}")
            print(f"  Students: {subject.num_students}")