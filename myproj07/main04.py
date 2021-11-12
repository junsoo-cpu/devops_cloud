from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 총 랭크 된 가수가 몇명인지?
# 1
artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)
print(len(artist_list))

# 2
artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
print(len(artist_set))

# 3
artist_set = set([song_dict["artist"] for song_dict in song_list])
print(len(artist_set))

# 4 : set Comprehension
artist_set = {song_dict["artist"] for song_dict in song_list}
print(len(artist_set))
