def find_max_number(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
            print(maximum)