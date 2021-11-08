# 숫자 퀴즈
import random

number = random.randint(1, 100)

for i in range(10):
    print(f"남은 기회 : {10-i}")
    guess = input("숫자를 입력하세요 :")
    answer = int(guess)

    if i == 9:
        print("다음 기회에...")
        break

    if answer == number:
        print(f"정답입니다.{i+1}번째에 맞추었습니다.")
        break

    elif answer < number:
        print("더 큰 수를 입력해주세요")
    elif answer > number:
        print("더 작은 수를 입력해주세요")
