import { useState } from "react";

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }
function dispatch(action, prevState) {
  // 순수함수로서 구현이 되어야만 합니다.
  // 같은 값의 인자가 주어지만, 항상 같은 값의 리턴을 해야만 하고
  // 인자 외에 다른 어떤 값, 어떤 통신을 해서도 안 됩니다.
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  // 버그 !!!
  return prevState;
}

function dispatch_color(action, prevState) {
  const { type, amount } = action;
  if (type === "GREEN") {
    return (prevState = amount);
  } else if (type === "BLUE") {
    return (prevState = amount);
  } else if (type === "RED") {
    return (prevState = amount);
  }
}

function Counter2() {
  // TODO: color와 value
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return dispatch(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  const handleGreen = () => {
    const action = { type: "GREEN", amount: "green" };
    setColor((prevColor) => {
      return dispatch_color(action, prevColor);
    });
  };

  const handleBlue = () => {
    const action = { type: "BLUE", amount: "blue" };
    setColor((prevColor) => {
      return dispatch_color(action, prevColor);
    });
  };

  const handleRed = () => {
    const action = { type: "RED", amount: "red" };
    setColor((prevColor) => {
      return dispatch_color(action, prevColor);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      <div style={{ backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleGreen}>그린</button>
      <button onClick={handleBlue}>블루</button>
      <button onClick={handleRed}>레드</button>
    </div>
  );
}

export default Counter2;
