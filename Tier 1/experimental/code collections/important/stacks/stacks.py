# Create an empty stack
stack = []

# Push items onto the stack
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack after pushes:", stack)

# Pop items from the stack (LIFO order)
top_item = stack.pop()
print("Popped item:", top_item)
print("Stack now:", stack)

top_item = stack.pop()
print("Popped item:", top_item)
print("Stack now:", stack)