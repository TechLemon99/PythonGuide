# NOTE: TO PLAY THE GAME, SIMPLY RUN python if.py IN THE SHELL.

#---------------------------------------------------

# The If Statement:

# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.

number = 69
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

# Remember that the elif and else parts are optional. A minimal valid if statement is:

if True:
    print('Yes, it is true')