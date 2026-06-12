# Create a 3x3 tic-tac-toe board
board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", " "]
]

# Print the board neatly
print("Tic-Tac-Toe Board:")
for i, row in enumerate(board):
    print(" | ".join(row))
    if i < len(board) - 1:
        print("-" * 9)  # separator line