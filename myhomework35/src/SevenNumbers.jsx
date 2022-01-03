import { useReducer } from 'react';

function reducer(state, action) {
  const { type } = action;
  if (type === 'GENERATE_NUMBERS') {
    return {
      ...state,
      numbers: makeNumbers(),
    };
  } else if (type === 'SHUFFLE_NUMBERS') {
    return {
      ...state,
      numbers: state.numbers.sort(() => Math.random() - Math.random()),
    };
  } else if (type === 'SHUFFLE_COLORS') {
    return {
      ...state,
      colors: state.colors.sort(() => Math.random() - Math.random()),
    };
  }
  return state;
}

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

  const generateNumbers = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };

  const shuffleNumbers = () => {
    dispatch({ type: 'SHUFFLE_NUMBERS' });
  };

  const shuffleColors = () => {
    dispatch({ type: 'SHUFFLE_COLORS' });
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      <button onClick={generateNumbers}>7개 숫자</button>
      <button onClick={shuffleNumbers}>숫자 섞기</button>
      <button onClick={shuffleColors}>색깔 섞기</button>
      <hr />
      {state.numbers.map((number, index) => {
        return (
          <div
            style={{
              ...defaultStyle,
              backgroundColor: state.colors[index],
            }}
          >
            {number}
          </div>
        );
      })}
    </div>
  );
}
export default SevenNumbers;

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
  margin: '1rem',
};
