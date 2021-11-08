from collections import Counter
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
교수님 코딩 방법(기본)
"""

# """ㄹ
# 방탄소년단의 곡명
# """
# for song_dict in song_list:
#     if song_dict["artist"] == "방탄소년단":
#         # print(song_dict["artist"], song_dict["title"], song_dict["like"])

#         line = "{}, {}, {}".format(
#             song_dict["artist"], song_dict["title"], song_dict["like"]
#         )
#         line = "{가수명}, {곡명}, {좋아요수}".format(
#             가수명=song_dict["artist"], 곡명=song_dict["title"], 좋아요수=song_dict["like"]
#         )
#         line = "{artist}, {title}, {like}".format(
#             artist=song_dict["artist"], title=song_dict["title"], like=song_dict["like"]
#         )
#         # unpack arguments
#         line = "{artist}, {title}, {like}".format(**song_dict)
#         print(line)
# # """
# 곡명에 가을이 들어가는 곡
# """
# for song_dict in song_list:
#     if "가을" in song_dict["artist"]:
#         print(song_dict["title"])

# """
# 좋아요 수가 20_0000이 넘는 곡수
# """
# song_count = 0
# for song_dict in song_list:
#     if song_dict["like"] > 200000:
#         song_count += 1
# print(f"좋아요 수가 200000이 넘는 곡은 {song_count}입니다.")

# """
# 가수별 곡 수
# """

# artist_dict = {}
# for song_dict in song_list:
#     artist: str = song_dict["artist"]

#     if artist not in artist_dict:
#         artist_dict[artist] = 0
#     artist_dict[artist] += 1

# print(artist_dict)


# # 같은 방법
# artist_list = []
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     artist_list.append

# # List Comprehension
# artist_list = [song_list["artist"] for song_dict in song_list]

# print(Counter(artist_list))
