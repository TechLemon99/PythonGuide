my_list = [2, 4, 5, "tomatoes", 6, 7]

for i in my_list:
    print(i, end=" ")

if 2 in my_list:
    print("\n2 exists within the list")

if "tomatoes" in my_list:
    print("tomatoes exists within the list")

if 3 in my_list:
    print("3 exists within the list")
else:
    print("3 does not exist within the list")

my_list[1] = 10 # change number at index 1 to new number: 10
print(my_list)