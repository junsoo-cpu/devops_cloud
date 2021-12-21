// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(
    function (song_list) {
        return song_list.like >= 200000
    });

result.sort(function (song1, song2) {
    return song1.title < song2.title ? -1 : song1.title > song2.title ? 1 : 0;
}) // 오름차순 정렬

for (const song of result) {
    console.log(song.like, song.title, song.artist)
}

// for (const song of result) {
//     console.log("[", song.like, "]", song.title, song.artist)
// }