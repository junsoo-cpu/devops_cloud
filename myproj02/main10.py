# import random
# import time

# animal_names = [
#     "cat",
#     "dog",
#     "fox",
#     "monkey",
#     "mouse",
#     "panda",
#     "frog",
#     "snake",
#     "wolf",
# ]

# input("준비되셨으면, 엔터키를 입력해주세요.")

# start_time = time.time()

# ok_counter = 0

# for count in range(5):
#     random_name = random.choice(animal_names)
#     #방법1 : 이미 사용된 random_name을 받았다면 다시 가져오는 것
#     print(random_name)
#     line = input(">>> ")
#     if random_name == line:
#         ok_counter += 1
#         print("정확합니다.")
#     else:
#         print("오타가 있어요.")

# end_time = time.time()

# print(f"{ok_counter}번 성공하셨습니다.")
# print(f"총 {end_time - start_time}초가 걸리셨어요")

# 분 당 타이핑 수
import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

random.shuffle(animal_names)
start_time = time.time()

ok_counter = 0
keyboard_counter = 0
# for count in range(5):
#     random_name = random.choice(animal_names)
# 방법 1 : 이미 사용된 random_name을 받았다면 다시 가져오는 것
for random_name in animal_names[0:5]:
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        keyboard_counter += len(random_name)  # 길이 값을 저장
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()

use_time = end_time - start_time  # 입력 걸린 시간
keyboard_speed = keyboard_counter / use_time * 60  # 분 당 타이핑 수

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {use_time}초가 걸리셨어요")
print(f"분 당 타이핑 속도는 {keyboard_speed} 입니다.")
