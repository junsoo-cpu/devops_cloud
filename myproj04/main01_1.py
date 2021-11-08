# 문자열을 인자로 받아, 단어수를 반환하는 함수
def get_word_count(s):
    return len(s.split(" "))


sentence = input("문장을 입력하세요 : ")
print(get_word_count(sentence))


# 문자열을 인자로 받아 공백을 제외한 글자를 반환하는 함수
def get_count(s):
    acc = []
    for i in s:
        if i != " ":
            acc.append(i)
    return len(acc)


sentence = "우리는 파이썬을 즐겨요"
print(get_count(sentence))

# 자연수를 인자로 받아, 천 단위 절사한 값을 리턴하는 함수
def send_1000(s):
    return s // 1000 * 1000


number = int(input(" 숫자를 입력하세요"))
print(send_1000(number))
