// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

song_array.sort((
    song_list1, song_list2) => song_list2.like - song_list1.like
);

song_list = song_array.slice(0, 10);

for (const song of song_list) {
    console.log(song.like, song.artist, song.title);
};