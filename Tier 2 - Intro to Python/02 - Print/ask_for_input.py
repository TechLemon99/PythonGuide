# The input funciton allows you to prompt the user for a value
# You need to declare a variable to hold the value entered by the user

name = input("enter ur name: ")
age = input("ENTER AGE: ")
print("hello " + name + " :) ru " + age + " years old?")
dee = input("yes [Y] or no [N]: ")

if dee.upper == "Y":
    print("ok etch")
else:
    print("ok")

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

print(f"{word1} and {word2} :)")