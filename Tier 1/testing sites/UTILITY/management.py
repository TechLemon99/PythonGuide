class Employee:
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name: str, employee_id: str, budget: float):
        super().__init__(name, employee_id)
        self.budget = budget
        self.subordinates = []

    def add_subordinate(self, employee: Employee):
        self.subordinates.append(employee)

class Developer(Employee):
    def __init__(self, name: str, employee_id: str, specialisation: str):
        super().__init__(name, employee_id)
        self.specialisation = specialisation

    def display_info(self):
        super().display_info()
        print(f"Specialisation: {self.specialisation}")

employee1 = Employee("Alice", "E001")
manager1 = Manager("Bob", "M001", 100000.0)
developer1 = Developer("Charlie", "D001", "Backend")

employee1.display_info()
manager1.display_info()
developer1.display_info()

manager1.add_subordinate(employee1)
print(f"Manager {manager1.name} has {len(manager1.subordinates)} subordinates.")
print("The subordinates are: ")
for subordinate in manager1.subordinates:
    print(f"- {subordinate.name} (ID: {subordinate.employee_id})")