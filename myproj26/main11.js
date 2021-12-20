const fs = require("fs");
const fsPromises = fs.promises;


// await는 promise 문법에 대한 축약
async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loaded : ", files);
    }
    catch (error) {
        console.error(error);
    }
}

main();

// 2 : Promise
// fsPromises.readdir("c:/Dev")
//     .then(files => console.log("loded :", files))
//     .catch(error => console.error(err));


// 1 : Callback
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// });

console.log("ENDED");