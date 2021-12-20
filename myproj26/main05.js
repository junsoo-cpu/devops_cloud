// // Array
// const [name] = ["Tom", 10, "Seoul"];

// // 변수명 생략 가능
// const [, age] = ["Tom", 10, "Seoul"];

// // heigh는 undefined
// // const [name, age, region, height] = ["Tom", 10, "Seoul"];

// // 값 할당에 실패했을 때 적용되는 디폴트 값
// const [name, age, region, height=140] = ["Tom", 10, "Seoul"];


// 디폴트 값을 함수 호출로 지정
function get_default_hieght() {
    console.log("get_default_hieght 함수를 호출했습니다.");
    return 140;
}
const [name, age, region, height = get_default_hieght()] = ["Tom", 10, "Seoul"]