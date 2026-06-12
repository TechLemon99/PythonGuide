def greet(name): # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice") # "Alice" is an argument passed to the 'name' parameter
greet("Bob")   # "Bob" is another argument

def kill(victim, protagonist, antagonist):
    print(f"{victim} was killed by {antagonist}, so {protagonist} killed {antagonist}")

kill("Ray Wing", "Axel Poo", "Gua Xi")