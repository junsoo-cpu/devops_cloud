for number in range(2, 10):
    print(f"---{number}단---")
    for i in range(1,10):
        print(f"{number} * {i} = {number * i}")
        if number == i:
            break
    print("")
