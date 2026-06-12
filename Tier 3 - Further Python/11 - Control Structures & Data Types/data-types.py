# strings, intergers, floats and booleans

string_data = str(input("type a string here: "))
integer_data = int(input("type an integer here: "))
float_data = float(input("type a float here: "))
boolean_data = bool(input("type a boolean here: "))
databool = True

list_data = list(input("Type list items here: "))
dictionary_data = {}
num_entries = int(input("Enter the number of entries you want to add: "))
for i in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary_data[key] = value

print("strings are anything that involves letters, grammar and text")
print(f"integers are whole numbers that can be manipulated using math functions {integer_data + 12/3}")
print(f"floats are any number, floats can be decimals, negatives and whole numbers {float_data/3.2*17.23+-3}")
if boolean_data and databool == True:
    print(f"boolean is true, false, and, or and not {boolean_data}")
else:
    print(f"boolean is true, false, and, or and not {databool}")
print(f"lists are collections that will have multiple peices of data inside it {list_data}")
print(f"dictionaries are collections that will create a key and assign a value to that key {dictionary_data}")