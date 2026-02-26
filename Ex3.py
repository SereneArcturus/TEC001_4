cities = []
for i in range(5):
    city = input("Type the name of the city here " + str(i + 1) + ": ")
    cities.append(city)
print()
print("These are cities that you entered:")

for city in cities:
    print(city)