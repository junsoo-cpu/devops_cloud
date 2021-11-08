import random

number = random.randint(1, 40)

if number < 10:
    print("1")
elif number < 20:
    print("10")
elif number < 30:
    print("20")
else:
    print("너무 큰 수")

print(f"숫자는 {number} 입니다.")
