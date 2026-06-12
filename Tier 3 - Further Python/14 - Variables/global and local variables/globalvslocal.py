global_var = 10  # A global variable

def access_global():
    print(f"Inside access_global: {global_var}") # Accessing global_var without 'global'

def modify_global_incorrectly():
    global_var = 20  # Creates a new local variable named global_var
    print(f"Inside modify_global_incorrectly (local): {global_var}")

def modify_global_correctly():
    global global_var  # Declares intent to modify the global variable
    global_var = 30
    print(f"Inside modify_global_correctly: {global_var}")

access_global()
modify_global_incorrectly()
print(f"Outside functions (after incorrect modification): {global_var}") # Global variable remains unchanged
modify_global_correctly()
print(f"Outside functions (after correct modification): {global_var}") # Global variable is now changed