numbers = int(input("Type an integer number here: "))
if numbers < 2:
    print("This is not a prime number, type another one that > 1")
else:
    for i in range(2, int(numbers ** 0.5) + 1):
        if numbers % i == 0:
            print("This number is not a prime number, hmu hmu")
            break
    else:
        print("This number is a prime number, yipee!")