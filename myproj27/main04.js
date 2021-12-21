// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(
    function (song) {
        return song.like >= 200000
    });

for (const song of result) {
    console.log(song.like, song.artist, song.title)
}