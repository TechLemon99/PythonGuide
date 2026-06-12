# get the add_numbers function from the add_numbers.py file
def add_numbers(a, b):
  return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is", result)


# word frequency
def word_frequency(sentence):
  words = sentence.split()
  frequency = {}
  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
  return frequency

sentence = input("Enter a sentence: ")
result = word_frequency(sentence)
print("Word frequency:", result)

# min and max
def min_max(numbers):
  return min(numbers), max(numbers)

input_numbers = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in input_numbers.split()]
result = min_max(numbers)
print("Lowest number:", result[0])
print("Highest number:", result[1])


# vowels and consonants
def count_vowels_consonants(string):
  vowels = "aeiouAEIOU"
  consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  vowels_count = 0
  consonants_count = 0
  for char in string:
    if char in vowels:
      vowels_count += 1
    elif char in consonants:
      consonants_count += 1
  return vowels_count, consonants_count

input_string = input("Enter a string: ")
result = count_vowels_consonants(input_string)
print("Number of vowels:", result[0])
print("Number of consonants:", result[1])



# random password
# import random module to generate random numbers
import random
# import string module to get all the characters
import string
# define a function to generate a random password
def generate_password(length):
    #
    letters = string.ascii_letters
    digits = string.digits
    password = random.choice(letters) + random.choice(digits)
    #
    for i in range(length - 2):
        password += random.choice(letters + digits)
    return password

