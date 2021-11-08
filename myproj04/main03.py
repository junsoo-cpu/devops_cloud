# 크롤링
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

# # 방탄소년단 곡 명만 출력
# for song in song_list:
#     if song["artist"] == "방탄소년단":
#         print(song["title"])

# # 곡 명에 "가을"이 들어가는 곡 출력
# for song in song_list:
#     if "가을" in song["title"]:
#         print(song["title"])

# # 좋아요 수가 200000이 넘는 곡 수
# count = 0
# for song in song_list:
#     if song["like"] > 20_0000:
#         count += 1
# print(count)


# 가수 별 곡 수
# singer = []
# for song in song_list:
#     singer.append(song["artist"])

# singer_1 = {}
# for ch in singer:
#     try:
#         singer_1[ch] += 1
#     except:
#         singer_1[ch] = 1
# print(singer_1)
