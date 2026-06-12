# Description: Example 2 - Find the maximum value in a list of numbers
def find_max_value(numbers_list):
    max_value = numbers_list[0]
    for number in numbers_list:
        if number > max_value:
            max_value = number
    return max_value

print(find_max_value([5, 10, 15, 20, 25]))
print(find_max_value([100, 200, 300, 400, 500]))
