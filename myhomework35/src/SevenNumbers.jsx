import { useReducer } from 'react';

const makeNumbers = () => {
  const randomNumber = [];
  while (randomNumber.length < 7) {
    const number = parseInt(Math.random() * 45) + 1;
    if (randomNumber.indexOf(number) < 0) {
      randomNumber.push(number);
    }
  }
  randomNumber.sort((a, b) => {
    return a - b;
  });
  return randomNumber;
};

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });

  return (
    <div>
      <h2>7개의 숫자</h2>
    </div>
  );
}
export default SevenNumbers;
