class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance of the Car object
my_car = Car("Toyota", "Camry", 2020)

# Print the initial year attribute
print(f"Initial year of my_car: {my_car.year}")

# Modify the year attribute using dot notation
my_car.year = 2023

# Print the modified year attribute
print(f"Modified year of my_car: {my_car.year}")