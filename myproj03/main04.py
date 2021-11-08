# 반복문을 활용하여, 효과적으로 3단/6단/9단 구구단 출력하기
for number in range(3, 10, 3):  # 3부터 시작, 10까지 3씩 증가
    print(f"---{number}단---")  # 단수
    for i in range(1, 10):  # 1부터 9까지 곱할 수 반복
        print(f"{number} * {i} = {number * i}")  # 곱셈 수식
    print("")  # 가독성을 위해 한칸 띄어줌

# 1이상 100미만 범위에서 3과 5의 공배수를 모두 출력하기
for number in range(1, 100):  # 1이상 100미만의 수
    if number % 3 == 0 and number % 5 == 0:  # 3의 배수와 5의 배수의 공배수
        print(number)  # 숫자 출력

# 1이상 100미만 범위에서 3과 5의 공배수 합을 출력하기
answer = 0  # 합의 초기 값
for number in range(1, 100):  # 1이상 100미만의 수
    if number % 3 == 0 and number % 5 == 0:  # 3과 5의 공배수
        answer += number  # 공배수의 합을 저장
print(answer)  # 합 출력

# 구구단 퀴즈 break 안쓴 버전
for number in range(2, 10):
    print(f"---{number}단---")
    for i in range(1, number + 1):  # 출력하는 곱셈식의 수를 단수 범위만큼 지정
        print(f"{number} * {i} = {number * i}")
    print("")
