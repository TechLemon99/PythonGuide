# Instructions  

These are 5 program examples which use inputs to perform so processing and give an output.

Create a new project 300-GettingInput and a new file called main.py

## Steps

- Read the purpose of the program
- look at the 'output' expected (this is how we test algorithms)
- Add these 5 exercises to the main.py file and run each one to check they output the expected test data.

## Exercise 1: Greeting Program

### Write a program that asks the user for their name and then prints a personalised greeting.

What's your name? John
Hello, John!

```python

name = input("What's your name? ")
print("Hello, " + name + "!")
```

## Exercise 2: Circle Area Program

### Write a program that calculates the area of a circle with a user-specified radius.


What's the radius of the circle? 10
The area of the circle is 314.16

```python
import math

radius = float(input("What's the radius of the circle? "))
area = math.pi * radius ** 2
print("The area of the circle is", round(area, 2))
```
- import math is an example of?
- math.pi means 'from math,use pi' - is that right?
- what does round do? is round a math function, if so, why isn't it math.round?


## Exercise 3: Average Program

### Write a program that prompts the user for three numbers and then calculates their average.

Enter first number: 10
Enter second number: 20
Enter third number: 30
The average of the numbers is 20.0

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the numbers is", average)
```
- what is a 'float'?
- what is an 'int'?


## Exercise 4: Celsius to Fahrenheit Program

Write a program that asks the user for a temperature in Celsius and converts it to Fahrenheit.


### What's the temperature in Celsius? 100
### The temperature in Fahrenheit is 212.0

```python
celsius = float(input("What's the temperature in Celsius? "))
fahrenheit = celsius + 9 / 5 + 32
print("The temperature in Fahrenheit is", fahrenheit)
```
- correct the logic error in this script

## 5: Word Count Program

Write a program that asks the user for a sentence and then prints the number of words in the sentence.

### Enter a sentence: The quick brown fox jumps over the lazy dog.
The sentence has 9 words.

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
num_words = len(words)
print("The sentence has", num_words, "words.")
```
  - what data type is 'sentence'?
  - is .split a built in python method?
  - what does .split() do?
  - what data type is 'words'
  - what does len() do?

# Congratulations!
