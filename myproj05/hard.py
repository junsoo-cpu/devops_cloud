import pandas as pd
"""
멜론 TOP 100에서 곡 명 단어 수
"""
print("멜론 TOP100 에서 곡 명 단어수 출력")

df = pd.read_csv("https://bit.ly/3nsLDXy")
#방법 1
song_list = list(df.T.to_dict().values())


def song_title(song_dict):
    return song_dict["title"], len(song_dict["title"].split())


song_word_list = list(map(song_title, song_list))
print(song_word_list)

# 방법 2
# def song_title(song_dict):
#     title = song_dict["title"]
#     return title


# def song_word(song_dict):
#     word = len((song_dict["title"]).split(" "))
#     return word


# song_title_list = list(map(song_title, song_list))
# song_word_list = list(map(song_word, song_list))
# song_dict = dict(zip(song_title_list, song_word_list))
# print(song_dict)

# """
# 멜론 TOP100에서 곡 명 단어 수 TOP 10
# """
# print("멜론 TOP100 에서 곡 명 단어수 TOP10 출력")


# def 정렬기준값을_만들어줄_함수(song_dict):
#     word = len((song_dict["title"]).split(" "))
#     return word


# def make(song_dict):
#     title = song_dict["title"]
#     return title


# sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)
# top_100 = list(map(make, sorted_song_list))
# print(top_100[0:10])

# """
# 좋아요 수가 가장 많은 곡, 적은 곡
# """
# print("좋아요 수가 가장 많은 곡은? 가장 적은 곡은?")


# def make_1(song_dict):
#     title = song_dict["like"]
#     return title


# max_like = max(song_list, key=make_1)
# min_like = min(song_list, key=make_1)

# print("좋아요가 가장 많은 곡 : {title} {like}".format(**max_like))
# print("좋아요가 가장 적은 곡 : {title} {like}".format(**min_like))


# """
# 곡 명 단어 수가 가장 많은 곡, 적은 곡
# """
# print("곡 명 단어 수가 가장 많은 곡은? 가장 적은 곡은?")


# def make_2(song_dict):
#     word = len((song_dict["title"]).split(" "))
#     return word


# max_word_count = max(song_list, key=make_2)
# min_word_count = min(song_list, key=make_2)
# print("단어 수가 가장 많은 곡 : {title} ".format(**max_word_count))
# print("단어 수가 가장 적은 곡 : {title} ".format(**min_word_count))


# """
# 곡 명 단어 수가 가장 많은 곡, 적은 곡
# """
# print("곡 명 단어 수가 가장 많은 곡은? 가장 적은 곡은?")


# def make_3(song_dict):
#     word = len((song_dict["title"]))
#     return word


# max_word_count = max(song_list, key=make_3)
# min_word_count = min(song_list, key=make_3)
# print("글자 수가 가장 많은 곡 : {title} ".format(**max_word_count))
# print("글자 수가 가장 적은 곡 : {title} ".format(**min_word_count))


# """
# 리스트에 랭크된 가수 팀
# """
# print("리스트에 랭크 된 가수는 총 몇 팀인가요?")


# def song_artist(song_dict):
#     return song_dict["artist"]


# song_artist_list = list(map(song_artist, song_list))
# song_set_artist_list = set(song_artist_list)
# print(f"{len(song_set_artist_list)}팀")


# """
# 리스트에 2곡 이상 랭크 된 가수 팀
# """
# print("리스트에 2곡 이상 랭크 된 가수는 총 몇 팀인가요?")

# from collections import Counter


# def song_artist(song_dict):
#     title = song_dict["artist"]
#     return title


# artist_list = list(map(song_artist, song_list))
# artist_count_list = Counter(artist_list)
# value_list = filter(lambda x: x > 1, artist_count_list.values())
# print(f"{len(list(value_list))}팀")


# """
# 방탄소년단 좋아요 총 합
# """
# print("방탄소년단의 좋아요 총 합은?")


# def song_artist_filter(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# def song_like(song_dict):
#     return song_dict["like"]


# result = list(map(song_like, filter(song_artist_filter, song_list)))
# print(sum(result))
