from fast_food import Cashier, FryCook, DriveThruCashier

# Creating instances
cashier = Cashier("Victor Guo", 1001, 15.50, 8, 3)
fry_cook = FryCook("Ray Wong", 1002, 16.00, 7, "French Fries", 2)
drive_thru_cashier = DriveThruCashier("Ronen Gupta", 1003, 15.75, 6, 5, "DT-01")

# Testing methods
print(cashier.clock_in())
print(fry_cook.prepare_food())
print(drive_thru_cashier.take_drive_thru_order("Burger & Fries"))
print(cashier.process_order("Combo Meal"))
print(fry_cook.deep_fry_food())
print(drive_thru_cashier.clock_out())
print(cashier.get_pay())
print(fry_cook.get_pay())
print(drive_thru_cashier.get_pay())