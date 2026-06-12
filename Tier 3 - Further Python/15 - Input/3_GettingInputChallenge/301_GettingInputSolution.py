color = input("What's your favorite color? ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The sum of", num1, "and", num2, "is", num1 + num2)
print("The difference of", num1, "and", num2, "is", num1 - num2)
print("The product of", num1, "and", num2, "is", num1 * num2)
print("The quotient of", num1, "and", num2, "is", num1 / num2)

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("The number of vowels in the sentence is", count)

import random

random_num = random.randint(1, 100)
print("A random number between 1 and 100 is:", random_num)

if random_num % 2 == 0:
    print(random_num, "is an even number.")
else:
    print(random_num, "is an odd number.")