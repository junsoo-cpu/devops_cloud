print('"좋아요" 수가 200,000 이상인 곡에 대해서, 곡명 가나다 순으로 정렬')
# 1안) 필터링을 먼저 하고, 필터링된 결과에 대해서 곡명 오름차순 정렬 (!!!)
# 2안) 곡명에 대한 오름차순 정렬을 먼저하고, 필터링

# TODO
def filter_fn4(song_dict):
    return song_dict["like"] > 200_000


def sort_fn4(song_dict):
    return song_dict["title"]


new_song_list = filter(filter_fn4, song_list)  # list 타입은 아닙니다.
new_song_list = sorted(new_song_list, key=sort_fn4)

for song_dict in new_song_list:
    print(song_dict["like"], song_dict["title"])
