# sequential code goes straight down
print("this")
print("code")
print("is sequential")

# selection code has branching paths
x = int(input("this will determine what path happens: "))

if x == 1:
    print("this is path one")
elif x == 2:
    print("this is path two")
else:
    print("this is path three")

# repetition code repeats over and over
inp = input("type your : ")
password = "12345678"
while inp not in password:
    print("wrong password")
    inp = input("type your password: ")
print("access granted")