import numpy as np

# Ask the user to input 7 temperatures
temps = []
for i in range(7):
    value = float(input(f"Enter temperature for day {i+1}: "))
    temps.append(value)

# Convert to numpy array
temps = np.array(temps)

# Calculations
highest = np.max(temps)
lowest = np.min(temps)
average = np.mean(temps)
median = np.median(temps)
range = np.ptp(temps)
sum = np.sum(temps)

# Output
print("\nTemperatures for the week:", temps)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Average temperature:", round(average, 2))
print("Median temperature:", round(median, 2))
print("Temperature range:", range)
print("Sum of temperatures:", sum)