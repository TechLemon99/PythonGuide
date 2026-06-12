import numpy as np  # Import NumPy library

# 1. Create a 2D NumPy array to represent sales data for each year.
# Each row represents a year, and each column represents a month's sales.
sales_data = np.array([
    [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],  # 2015 sales data
    [1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150],  # 2016 sales data
])

# 2. Print the sales for the second year (index 1).
# Output will be the sales for 2016
print("\n2016 sales:")
print(sales_data[1])

# 3. Change the sales for July in the first year (2015) to a new value.
# Set July sales for 2015 to 1650
sales_data[0, 6] = 1650
print("\nAfter updating July 2015 sales:")
print(sales_data)

# 4. Add a new row for another year (2017).
# Note: NumPy arrays have fixed size, so to add new rows, use np.append or recreate the array.
new_year = np.array([int(x * 1.05) for x in sales_data[1]])  # 5% growth
sales_data = np.vstack([sales_data, new_year])  # Add new row

# 5. Print the updated sales data.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
years = ['2015', '2016', '2017']

print("\nFinal sales data with labels:")
print("Month\t" + "\t".join(months))
for i, year in enumerate(years):
    print(f"{year}\t" + "\t".join(map(str, sales_data[i])))