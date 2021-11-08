# sort
# number_list = [25, 19, 45, 32]

# def sort_fn(v): # 1의 자리를 기준으로 오름차순
#     return v % 10

# print(sorted(number_list, key=sort_fn))


# import pandas as pd # 내림차순 곡 목록
# df = pd.read_csv("https://bit.ly/3nsLDXy")
# song_list = list(df.T.to_dict().values())

# # 정렬을 하기 위해 각 값들에 대한 대소 비교가 가능해야 한다.
# # 10 < 100 , '가' < '나'

# def 정렬기준을_만들어줄_함수(song_dict):
#     return song_dict["like"]
#     pass

# for song_dict in sorted(song_list, reverse=True, key=정렬기준을_만들어줄_함수):
#     print("[{like}][{title}][{artist}]".format(**song_dict))


# 좋아요 top10만 출력
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

for song_dict in sorted_song_list[0:10]:
    print("[{like}] {title} {artist}".format(**song_dict))
