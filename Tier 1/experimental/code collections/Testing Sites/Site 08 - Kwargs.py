def greet_person(**kwargs):
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")
    if "age" in kwargs:
        print(f"You are {kwargs['age']} years old.")

# Print name and age but not city
greet_person(name="Victor", age=16, city="Bunda Town")