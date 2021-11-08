"""
"방탄소년단" 곡명만 출력하기
곡명에 "사랑"이 포함된 곡명만 출력하기
"좋아요" 수가 200,000 이상인 곡명만 출력하기
"""

from typing import List  # Type Hinting
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
"방탄소년단"의 곡명 문자열로 구성된 리스트를 만들어보세요.
"""

# title_list: List[str] = []
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         title: str = song_dict["title"]
#         title_list.append(title)

# print(title_list)
# def check_bts_song(song_dict):  # bts 노래라면 True 아니라면 False를 리턴
#     """bts 노래라면 True를 반환합니다"""
#     artist: str = song_dict["artist"]
#     return artist == "방탄소년단"


# # new_song_list = list(filter(check_bts_song, song_list))
# # print(new_song_list)

# # 단순히 print만 한다라고 한다면
# for song_dict in filter(check_bts_song, song_list):
#     print("{title}".format(**song_dict))  # ** 사전 안 title만 출력


"""
곡 명에 사랑이 포함된 곡들의 곡명 리스트를 만들어보세요
"""

# title_list: List[str] = []

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     if "사랑" in title:
#         title_list.append(title)

# print(title_list)


# def check_contains_love(song_dict):
#     title: str = song_dict["title"]
#     return "사랑" in title


# for song_dict in filter(check_contains_love, song_list):
#     print("{rank}, {title}".format(**song_dict))

# """
# "좋아요" 수가 200,000 이상인 곡들의 곡명 리스트를 만들어보세요.
# """

# title_list: List[str] = []

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     if like >= 200_000:
#         title_list.append(title)

# print(title_list)


def check_above_200000(song_dict):
    like: int = song_dict["like"]
    return like >= 2000000


for song_dict in filter(check_above_200000, song_list):
    print("{title}, {like}".format(**song_dict))
