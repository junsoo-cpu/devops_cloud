// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const { melon_data: song_array } = require("./melon_data");


const word_list = song_array.map(function (song) {
    let str = song.title.split(' ');
    return [song.title, str.length];
});

console.log(word_list);