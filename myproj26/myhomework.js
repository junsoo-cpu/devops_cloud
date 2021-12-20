const { question } = require("readline-sync");

const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]


function shuffle(array) { array.sort(() => Math.random() - 0.5); }
const shuffled_animal_names = animal_names; shuffle(animal_names);

const slice_names = shuffled_animal_names.slice(0, 5);

const begin_time = new Date();

let ok_counter = 0;

for (random_name of slice_names) {
    console.log(random_name);
    const line = question("입력 >>> ");

    if (line === random_name) {
        ok_counter++;
        console.log("정확해요!");
    }
    else {
        console.log("땡!");
    }
}

const end_time = new Date();

const time = (end_time.getTime() - begin_time.getTime()) / 1000;

console.log(`${ok_counter}번 성공!`);
console.log(`총 ${time}초가 걸렸어요!`);