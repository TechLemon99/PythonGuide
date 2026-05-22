print("Welcome to Lemon Media Center!")

while True:
    user = input("Enter a username (can only be all lowercase) > ")

    if user != user.lower():
        print("Username can only be lowercase letters!")
    else:
        break

while True:
    password = input("Enter a password (must be at least 12 characters long) > ")
    if len(password) < 12:
        print("Password must be at least 8 characters long!")
    else:
        break

print(f"Account created! Welcome, {user}!")