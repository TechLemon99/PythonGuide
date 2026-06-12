import math

data = ["Gua Xi", "RayWing", "AxelPoo", "Gupta", "Tamalam", "Big Lev", "Gay Gao", "Deez", "Lil G"]
n = len(data)

running = True
print(f"Loaded list with {n} choices: {data}")

while running:
    major_input = input("Would you like to see permutations or combinations (P/C): ").strip().lower()
    if major_input == "p":
        p_input = input("How many permutes (1-9) or type 'exit': ").strip().lower()

        if p_input == "exit":
            print("Goodbye")
            running = False
        else:
            try:
                r = int(p_input)
                if r <= 0 or r > 9:
                    print("Invalid number. Please choose between 1 and 9.")
                else:
                    npr = math.factorial(n) // math.factorial(n - r)
                    print(f"Permutations ({n} permute {r}): {npr}")
            except ValueError:
                print("Invalid input. Please enter a number or 'exit'.")
    elif major_input == "c":
        c_input = input("How many choices (1-9) or type 'exit': ").strip().lower()
        
        if c_input == "exit":
            print("Goodbye")
            running = False
        else:
            try:
                r = int(c_input)
                if r <= 0 or r > 9:
                    print("Invalid number. Please choose between 1 and 9.")
                else:
                    ncr = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
                    print(f"Combinations ({n} choose {r}): {ncr}")
            except ValueError:
                print("Invalid input. Please enter a number or 'exit'.")
    else:
        print("Invalid.")