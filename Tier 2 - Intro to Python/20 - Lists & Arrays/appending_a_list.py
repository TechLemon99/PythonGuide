cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Hobart", "Darwin", "Canberra", "Gold Coast", "Newcastle"]

print(cities)

visited_cities = []

desination=input("Enter the city you have visited: ")

while desination != "":
    if desination in cities:
        visited_cities.append(desination)
    else:
        print("Invalid city")
    desination=input("Enter the city you have visited: ")

print("You have visited the following cities: ")
for city in visited_cities:
    print(city)