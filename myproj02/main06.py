# def gugudan(number):
#     #number = 2
#     print(f"### {number}단 ###")
#     for i in range(1, 10):
#         print(f"{number} * {i} = {number * i}")


# gugudan(2)
# gugudan(3)
# gugudan(4)


def gugudan(number):
    print(f"### {number}단 ###")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


for i in range(2, 10):
    gugudan(i)
