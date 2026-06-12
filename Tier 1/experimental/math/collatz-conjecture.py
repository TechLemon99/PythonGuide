def collatz_sequence(n):
    """
    Generates and prints the Collatz sequence for a given positive integer.

    Args:
        n: A positive integer to start the sequence.
    """

    print(f"Collatz sequence for {n}:")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = (3 * n) + 1
        sequence.append(n)
    print(f"{sequence}\n")

while True:
    print("Enter a number, and I will run it with the principles of the Collatz Conjecture")
    print("Or type 'e' to exit")
    n_choice = input(">>>> ").lower()

    if n_choice == "e":
        print("Exiting the program.")
        break
    else:
        if n_choice.isdigit() and int(n_choice) > 0:
            n_choice = int(n_choice)
            collatz_sequence(n_choice)
        else:
            print("Please input a valid positive number\n")