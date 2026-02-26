def sum_list(numbers):
    return sum(numbers)

def main():
    my_list = []
    for i in range(5):
        number = int(input("Type the number " + str(i + 1) + " here : "))
        my_list.append(number)
    result = sum_list(my_list)
    print("This is the sum of the list that you typed:", result)

main()