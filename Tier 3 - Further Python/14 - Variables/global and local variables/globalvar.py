global_var = 10  # Global variable

def my_function():
    global global_var
    local_var = 5  # Local variable
    print(f"Inside function: global_var = {global_var}, local_var = {local_var}")

    # Modifying global_var (requires 'global' keyword)
    global_var = 20

my_function()
print(f"Outside function: global_var = {global_var}")
# print(local_var) # This would raise a NameError as local_var is out of scope