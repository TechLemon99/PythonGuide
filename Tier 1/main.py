# Swaroop - A Byte Of Python - Code Learning Session
# By ProLemon99

# Module 1: First Steps
print("hi")

lemon = "portugal"
print(lemon)

# Module 2: Basics
name = 'levin'
age = 12

print('{0} is {1} years old as of Jan 2022'.format(name, age))
print(f'{name} is {str(age)} years old as of Jan 2022') # Note these 2 are the same, f string came out as of Py 3.6
print(name + ' is ' + str(age) + ' years old as of Jan 2022') # This works too

# Module 3: Operators and Expressions
a = 2
a = a * 3
print(a)

a = 2
a *= 3
print(a) # These 2 are the same

# Notice that var = var operation expression becomes var operation= expression

# lambda = Lambda Expression
# if - else: Conditional Expression
# or - BOOLEAN or
# and - BOOLEAN and
# not x : Boolean NOT
# in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, including membership tests and identity tests 
# | : Bitwise OR
# ^ : Bitwise XOR
# & : Bitwise AND
# <<, >> : Shifts
# +, - : Addition and subtraction
# *, /, //, % : Multiplication, Division, Floor Division and Remainder
# +x, -x, ~x : Positive, Negative, bitwise NOT
# ** : Exponentiation
# x[index], x[index:index], x(arguments...), x.attribute : Subscription, slicing, call, attribute reference
# (expressions...), [expressions...], {key: value...}, {expressions...} : Binding or tuple display, list display, dictionary display, set display

# You can specify multi-line strings using triple quotes - (""" or '''). You can use single quotes and double quotes freely within the triple quotes. An example is:

'''This is a multi-line string. 
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

# What Python does in the format method is that it substitutes each argument value into the place of the specification. There can be more detailed specifications such as:

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} plays {book}'.format(name='pixel', book='roblox'))

# Since we are discussing formatting, note that print always ends with an invisible "new line" character (\n) so that repeated calls to print will all print on a separate line each. To prevent this newline character from being printed, you can specify that it should end with a blank:

print('a', end='')
print('b', end='')
# Or end with space
print('a', end=' ')
print('b', end=' ')
print('c')

# Strings
s = 'This is a string. \
This continues the string.'
print(s)
# is the same as:
s = 'This is a string. This continues the string.'
print(s)

# Indentations:

# Whitespace is important in Python. Actually, whitespace at the beginning of the line is important. This is called indentation. Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements. This means that statements which go together must have the same indentation. Each such set of statements is called a block. We will see examples of how blocks are important in later chapters.

# Error below! Notice a single space at the start of the line

# i = 5
 # print('Value is', i)
# print('I repeat, the value is', i)

#  File "whitespace.py", line 3
#    print('Value is', i)
#    ^
#IndentationError: unexpected indent

# Notice that there is a single space at the beginning of the second line. The error indicated by Python tells us that the syntax of the program is invalid i.e. the program was not properly written. 
# What this means to you is that you cannot arbitrarily start new blocks of statements (except for the default main block which you have been using all along, of course). 
# Cases where you can use new blocks will be detailed in later chapters such as the control flow.