# Description:  Example 3 - Passing a value to a function
def change_value(value):
    value = value + 10
    return value

a = 5
print(a)
a = change_value(a)
print(a)
