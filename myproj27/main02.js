// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(
    function (song) {
        return song.artist == "방탄소년단"
    });

for (const song of result) {
    console.log(song.artist, song.title, song.like)
}