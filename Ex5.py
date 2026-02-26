def remove_odd(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
    original_list = []

    numbers = input("Type numbers here, remember separated them by press spaces for good looking ^^: ").split()
    for num in numbers:
        original_list.append(int(num))
    new_list = remove_odd(original_list)

    print("This is the original list:", original_list)
    print("This is the list after removing odd numbers:", new_list)

main()