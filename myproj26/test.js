const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('What do you think of Node.js? ', (answer) => {
    console.log(`Thank you for your valuable feedback: ${answer}`);
    rl.close();
});

// var array = ['포도', '사과', '바나나', '망고'];

// for (var i in array) {
//     alert(array[i]);
// }

// const question = require('readline');
// const rl = question.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// const number = question("Enter a number : ");
// console.log(number)