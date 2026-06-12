# variables
x = "this is a variable"

# print command
print("this with send a message")

# inputs
x = input("this is where you can get the user to type stuff: ")

# if, elif and else
if x == "this is a variable":
    print("try changing the variable and see the result")
elif x == "something":
    print("this will only happen when both the if is false and the elif is true")
else:
    print("this will happen when both the if and elif are false")

# functions
def define():
    print("defining something will shorten code and make things easier by making a section of code one line")
define()

# dictionaries
mydictionary = {
    "a dictionary":1,
    "assigns a key": "and a value",
    "and act": "as extended variables"
}
print(mydictionary["a dictionary"])

# while loop
while x == "while":
    print("while loops will continue to loop until the condition is false")
    x = input("this is where you can get the user to type stuff: ")

# for in range loop
for n in range(6):
    print(n)

# lists
mylist = ["this", "is", "a", "list"]
print(mylist[0])
mylist.append(1)
print(mylist)

# classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

try:
    print(Person)
except:
    print("error!")
else:
    print("nothing's wrong")

# tuples
mytuple = ("apple", "banana", "cherry")
for i in mytuple:
  print(i)

# counting
x = "this will output the number of items in a string or list"
print(len(x))

# splitting
inp = input("this will become a list ")
inp.split()
print(inp)

# replacing strings
inp = input("your input will be changed ")
inp = inp.replace(inp[0:], "this has replaced your input")
print(inp)

# sorting
mylist = ["this", "will", "be", "sorted"]
mylist.sort()
print(mylist)

# equal and not equal to
inp = int(input("Number? "))
if inp == 3:
    print("that is equals to")
elif inp != 5:
    print("that is not equal to")

# data types
data = input("input in any data type: ")
print(type(data))

# unpacking tuples
tuple1 = ("this", "will", "be", "unpacked", "and", "become", "a", "variable")
(it, will, be, assigned, here) = tuple1
print(it)
print(will)
print(be)
print(assigned)
print(here)

# looping tuples
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# count instances in a tuple
mytuple = ("things", "in", "here", "will", "be", "repeated", "repeated")
counted = mytuple.count("repeated")
print(counted)

# search for a specific item
thistuple = ("this", "has", "been", "found")
searching = thistuple.index("found")
print(searching)

# sets
set1 = {"this", "is", "a", "set"}
print(set1)

# adding to sets
thisset = {"hello","there","good",}
thisset.add("morning")
print(thisset)

# clearing a set
myset = {"this", "will", "disappear"}
myset.clear()
print(myset)

# merging sets
set2 = {"this", "will"}
set3 = {"be", "merged"}
z = set2.intersection(set3)
print(z)

# Turning iterables into iterators
best_tuple = ("this", "will", "become", "an", "iterator")
iterate = iter(best_tuple)

# Getting the next value in an iterator
this_tuple = ("I'm","next","no","I","am")
print(next(this_tuple))