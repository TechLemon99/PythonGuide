# 5. Stacks Activity: Simulate the undo feature in a text editor. 
# Create an empty stack. 
# Ask the user to “type” words (push them onto the stack). 
# When the user types “undo”, pop the last word and show the updated sentence. 
# Extension: allow “redo” with another stack.

# Stack to hold words
undo_stack = []

running = True

while running:
    action = input("Type a word (or 'undo' to remove last word, 'exit' to quit): ").strip()
    
    if action.lower() == "undo":
        if undo_stack:
            removed_word = undo_stack.pop()
            print(f"Removed '{removed_word}'")
        else:
            print("Nothing to undo.")
    elif action.lower() == "exit":
        running = False
    else:
        undo_stack.append(action)
    
    # Show the current sentence
    print("Current sentence:", " ".join(undo_stack))