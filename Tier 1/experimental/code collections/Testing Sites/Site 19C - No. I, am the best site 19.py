subjects = ["English", "Software", "Drama", "Science", "Sport"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

while True:
    day_input = input("Which day? (or type 'exit' to quit): ").strip().capitalize()
    
    if day_input == "Exit":
        print("Ending program.")
        break
    elif day_input not in days:
        print("Invalid day. Please enter a valid weekday (e.g., Monday).")
        continue
    
    # Find the index of the day in the list (Monday=0, Tuesday=1, etc.)
    day_index = days.index(day_input)
    
    print(f"\nTimetable for {day_input}")
    
    # For each period (1 to 5), calculate the correct subject
    for period in range(5):
        # The subject index is calculated using modulo arithmetic to "rotate" the list.
        # For a given day (day_index) and period (p), the subject is at position:
        # (p - d) % 5. This creates the shifting pattern.
        subject_index = (period - day_index) % 5
        subject = subjects[subject_index]
        print(f"Period {period + 1}: {subject}")
    print()  # Add a blank line for readability