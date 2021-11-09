from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 각 곡명에 대한 단어 개수에 대한 TOP100
def pick_word_count_for_title(song_dict):
    title: str = song_dict["title"]
    title.split()
    word_list = title.split()
    return len(word_list)


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list

for song_dict in top10_song_list:
    print("{like} {title}".format(**song_dict))
