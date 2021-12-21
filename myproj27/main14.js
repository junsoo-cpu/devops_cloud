// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const { melon_data: song_array } = require("./melon_data");

const result = song_array.filter(
    function (song) {
        return song.artist == "방탄소년단"
    });

const like_list = result.map(function (song) {
    return [song.title, song.like]
})

let map = new Map(like_list)

console.log([...map.entries()].reduce((pv, cv) => pv[1] > cv[1] ? cv : pv)[0]);