// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// rl.question('What do you think of Node.js? ', (answer) => {
//     console.log(`Thank you for your valuable feedback: ${answer}`);
//     rl.close();
// });

numbers = [1, 2, 3, 4, 5];

const numbers1 = [31, 89, 24, 81, 46]

// // 내장 함수 map
// const new_number = numbers.map(
//     number => number ** 2
// );
// console.log(new_number);


// Array의 sort
function make_random_value(number) {
    return Math.random();
}

const new_numbers = numbers.map(
    (number) => ({ number, 기준값: Math.random() }
    ),
).sort(
    (value1, value2) => {
        return value1.기준값 - value2.기준값
    }
)

console.log(new_numbers)


// 대표님 방식

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
];

// const random_animal_names = animal_names
//     .map((name) => ({
//         name,
//         value: Math.random(),
//     }))
//     .sort((obj_a, obj_b) => {
//         return obj_a.value - obj_b.value;
//     })
//     .map(obj => {
//         return obj.value;
//     });

const shuffled_animal_names = animal_names
    .map((name) => ({
        name,
        value: Math.random(),
    }))
    .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value;
    })
    .map(({ name }) => name);

const begin_time = new Date().getTime();  // float
let ok_counter = 0;

for (const animal_name of shuffled_animal_names.slice(0, 5)) {
    const line = question(`${animal_name} >>> `);
    if (line === animal_name) {
        ok_counter++;
    }
}

const end_time = new Date().getTime();   // float

const time = end_time - begin_time;
console.log(`총 ${parseInt(time / 1000)}초가 소요되었습니다.`);

console.log(`총 ${ok_counter}회 맞추셨습니다.`);