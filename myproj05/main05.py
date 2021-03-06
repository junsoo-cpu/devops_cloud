# TDD 테스트 주도 개발
def make_powered_list(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers



def make_powered_list2(numbers):
    make_power = lambda number: number **2
    return map(make_power, numbers)