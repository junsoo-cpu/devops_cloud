import { useState, useReducer } from 'react';
import './Counter.css';

function reducer(prevState, action) {
  const { type, amount } = action;
  if (type === 'PLUS') {
    return prevState + amount;
  }
  return prevState;
}

function Counter() {
  // const [value, setValue] = useState(0);
  const [state, dispatch] = useReducer(reducer, 0);

  // const handleclick = () => {
  //   setValue(value + 1);
  // };

  // const handleRightClick = (e) => {
  //   e.preventDefault();
  //   setValue(value - 1);
  // };

  const reducerPlusState = () => {
    const action = { type: 'PLUS', amount: 1 };
    dispatch(action);
  };

  const reducerMinusState = () => {
    const action = { type: 'PLUS', amount: -1 };
    dispatch(action);
  };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={reducerPlusState}
      onContextMenu={reducerMinusState}
      // onClick={handleclick}
      // onContextMenu={handleRightClick}
    >
      {state}
      {/* {value} */}
    </div>
  );
}

export default Counter;
