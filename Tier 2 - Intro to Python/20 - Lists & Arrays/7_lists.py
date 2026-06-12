# This program will use lists to store multiple values
heros = ["tracer", "hanzo", "McCree    "]
print(heros[1]) # Output: tracer
print(heros[2]) # Output: hanzo
print(heros[3]) # Output: McCree

#add a loop to print all the heros
for hero in heros:
    print(hero)

# if you want to add a new hero to the list

heros.append("Genji")
print(heros)

# if you want to remove a hero from the list
heros.remove("McCree")

# if you want to remove a hero from the list by index
heros.pop(1)

# if you want to sort the list 
heros.sort()

# if you want to reverse the list
heros.reverse()

# if you want to get the length of the list
print(len(heros))

# if you want to get the index of a hero
print(heros.index("Genji"))

# if you want to change the value of a hero
heros[0] = "Tracer"

#if you want to copy a list
heros2 = heros.copy()

# if you want to clear the list
heros.clear()

# if you want to join two lists
heros3 = heros + heros2

# if you want sort the list in reverse order
heros.sort(reverse=True)

#if you want to get the last hero in the list
print(heros[-1])

# if you want to get the last two heroes in the list
print(heros[-2:])

# if you want to get the first two heroes in the list
print(heros[:2])

# if you want to get the first two heroes in the list
print(heros[0:2])

#if you want check if a hero is in the list
print("Tracer" in heros)
# Output: True

# if you want check if a hero is not in the list
print("Tracer" not in heros)
# Output: False

#if you want to sort the list alphabetically
heros.sort()

#if you want to add a new hero to the list in a specific index
heros.insert(1, "Hanzo")

# if you want to remove a hero from the list by index
heros.pop(1)


