// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(
    function (song) {
        return song.like >= 200000
    });

const result_list = result.map(function (song) {
    return song.title
})
console.log(result_list);