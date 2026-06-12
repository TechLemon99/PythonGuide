# Base class
class Employee:
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}")

# Subclass of Employee
class Manager(Employee):
    def __init__(self, name: str, employee_id: str, budget: float):
        super().__init__(name, employee_id)
        self.budget = budget
        self.subordinates = []  # List of Employee objects

    def add_subordinate(self, employee: Employee):
        self.subordinates.append(employee)

    def display_info(self):
        # Print manager info
        print(f"Manager: {self.name}, ID: {self.employee_id}, Budget: {self.budget}")
        # Print subordinate info
        print("Subordinates:")
        if self.subordinates:
            for emp in self.subordinates:
                print(f"  - {emp.name} (ID: {emp.employee_id})")
        else:
            print("  None")

# Subclass of Employee
class Developer(Employee):
    def __init__(self, name: str, employee_id: str, specialisation: str):
        super().__init__(name, employee_id)
        self.specialisation = specialisation

    def display_info(self):
        print(f"Developer: {self.name}, ID: {self.employee_id}, Specialisation: {self.specialisation}")

# --- Example usage ---
if __name__ == "__main__":
    # Create employees
    dev1 = Developer("Alice", "D101", "Backend")
    dev2 = Developer("Bob", "D102", "Frontend")
    mgr = Manager("Charlie", "M201", 100000)

    # Add subordinates
    mgr.add_subordinate(dev1)
    mgr.add_subordinate(dev2)

    # Display info
    mgr.display_info()
    dev1.display_info()
    dev2.display_info()