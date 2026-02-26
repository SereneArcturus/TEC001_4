numbers = []
while True:
    input_from_user = input("Type a number here (if you want to quit, just press Enter): ")
    if input_from_user == "":
        break
    try:
        number = float(input_from_user)
        numbers.append(number)
    except ValueError:
        print("That's wrong typing. Try again with a valid number.")

numbers.sort(reverse=True)
print("These are 5 greatest numbers, from high to low:")
for num in numbers[:5]:
    print(num)