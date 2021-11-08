# filter


def check_even_number(number):
    return number % 2 == 0


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in filter(check_even_number, numbers):
    print(number)
