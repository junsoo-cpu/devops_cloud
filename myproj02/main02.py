answer = input("12 + 23 = ")

# answer로 계산할 목적이라면, 값 변환은 최대한 빠르게 수행
answer = int(answer or 0)  # -> 앞 문자열이 거짓이라면 0을 사용

if answer == 35:
    print("정답")
else:
    print("땡")
