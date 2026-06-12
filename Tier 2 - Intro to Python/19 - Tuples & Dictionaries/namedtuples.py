# Keywords Argument Version
from collections import namedtuple

bruh = namedtuple("Car", ["model", "speed_kmh", "luxury", "year", "country"])

car_example1 = bruh(model="Tesla Model S", speed_kmh=250, luxury=True, year=2020, country="USA")

print(car_example1.model)
print(car_example1.speed_kmh)
print(car_example1.luxury)
print(car_example1.year)
print(car_example1.country)

# Positional Argument Version
from collections import namedtuple 

bruh2 = namedtuple("Car", ["model", "speed_kmh", "luxury", "year", "country"])

car_example2 = bruh2("Tesla Model S", 250, True, 2020, "USA")

print(car_example2.model)
print(car_example2.speed_kmh)
print(car_example2.luxury)
print(car_example2.year)
print(car_example2.country)