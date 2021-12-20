const tom = {
    name: "Tom",
    age: 10,
    region: "Daejeon",
}

// // const name = tom.name;
// // const age = tom["age"];

// const { name, age } = tom;
// console.log(name, age);

const { name: otherName } = tom;
console.log(otherName);

const steve = {
    name: {
        first: "Steve",
        last: "Jobs",
    },
    age: 10,
    region: "dajeon",
};

const { name: otherName2 } = steve;
console.log(otherName2);

const { name: { first } } = steve;
console.log(first);

const { name: { first: firstname } } = steve;
console.log(firstname);