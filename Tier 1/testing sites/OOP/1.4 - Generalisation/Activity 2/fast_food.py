class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.clocked_in = False

    def clock_in(self):
        self.clocked_in = True
        return f"{self.name} (ID: {self.employee_id}) has clocked in."

    def clock_out(self):
        self.clocked_in = False
        return f"{self.name} (ID: {self.employee_id}) has clocked out."

    def get_pay(self):
        return f"{self.name}'s total pay for the shift: ${self.hourly_wage * self.shift_hours:.2f}"

class Cashier(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, register_number):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.register_number = register_number

    def process_order(self, order):
        return f"{self.name} has processed order: {order} at Register {self.register_number}."

class Cook(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, specialty):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.specialty = specialty

    def prepare_food(self):
        return f"{self.name} is preparing {self.specialty}."

class Cleaner(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, cleaning_area):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.cleaning_area = cleaning_area

    def sanitize_area(self):
        return f"{self.name} is sanitizing {self.cleaning_area}."
    
# Derivative Subclasses
class DriveThruCashier(Cashier):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, register_number, headset_id):
        super().__init__(name, employee_id, hourly_wage, shift_hours, register_number)
        self.headset_id = headset_id

    def take_drive_thru_order(self, order):
        return f"{self.name} is taking a drive-thru order: {order} with Headset {self.headset_id}."

class FryCook(Cook):
    def __init__(self, name, employee_id, hourly_wage, shift_hours, specialty, fry_station_number):
        super().__init__(name, employee_id, hourly_wage, shift_hours, specialty)
        self.fry_station_number = fry_station_number

    def deep_fry_food(self):
        return f"{self.name} is deep frying {self.specialty} at Station {self.fry_station_number}."