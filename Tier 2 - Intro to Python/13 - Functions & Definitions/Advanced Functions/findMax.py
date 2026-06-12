numbers = [2, 4, 6, 8, 5]

def findMaximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        else:
            num = numbers[0]
    return max_value

print(findMaximum(numbers))