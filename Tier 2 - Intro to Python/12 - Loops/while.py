# The while statement

# The while statement allows you to repeatedly execute a block of statements as long as a condition is true.
# A while statement is an example of what is called a looping statement. 
# A while statement can have an optional else clause.

# The True and False are called Boolean types and you can consider them to be equivalent to the value 1 and 0 respectively.

# -----------------------------------------------------------------------------------------------------------------------------

# Example 1
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
	print(names[index])
	# Change the condition!!
	index += 1

# Example 3  
while True:
    choice=input('press Y or N to continue: ')
    #convert the choice to lower case
    choice=choice.lower()

    if choice=='y':
        print('You chose to continue')
        break
    elif choice=='n':
        print('You chose to quit')
        break
    else:
        print('I do not understand that choice')

print("Game over!")