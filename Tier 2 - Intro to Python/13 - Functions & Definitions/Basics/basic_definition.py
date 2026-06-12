# functions allow you to compress peices of code that may need to be used multiple times
def do_smth():
    print("this did something")
do_smth()

# functions can have parameters that can be called on as a variable when writing the code within the function and will be defined when called
def data_show(number, kind):
    print(f"{kind} has {number} instances")
data_show(7, "water")