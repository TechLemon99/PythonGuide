def right(m, n):
    return m[-n:] if n > 0 else ""

def Shorten():
    phrase = input("Phrase > ")
    phrase = phrase + "X"  # Adds an X to the end of phrase
    Len = len(phrase)
    NewPhrase = " "
    while True:  # REPEAT (outer loop)
        done = False
        NewPhrase = NewPhrase + phrase[0]  # 1st character of phrase
        
        while not done:  # REPEAT (inner loop)
            if phrase[0] != phrase[1]:  # IF 1st character ≠ 2nd character
                done = True
            Len = Len - 1
            phrase = right(phrase, Len)
            # UNTIL done = TRUE (handled by while not done)
        # END inner loop
        
        if Len < 1:  # UNTIL Len < 1
            break
    # END outer loop
    
    print(phrase)  # output phrase
    phrase = NewPhrase  # This line is useless since function ends here

# Call the function
Shorten()