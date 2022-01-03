import { useState, useReducer } from "react";

function reducer(prevState, action) {
  const { type, amount, color } = action;
  if (type === "PLUS") {
    return {
      ...prevState,
      value: prevState.value + amount,
    };
  } else if (type === "MINUS") {
    return {
      ...prevState,
      value: prevState.value - amount,
    };
  } else if (type === "CHANGE_COLOR") {
    return {
      ...prevState,
      color,
    };
  }
  return prevState;
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { value: 0, color: "red" });

  // 상탯값 정의
  // const [value, setValue] = useState(0);
  // const [color, setColor] = useState("red");

  // 상탯값 변경하는 함수들
  // const handlePlus = () => {
  //   setValue((prevValue) => prevValue + 1);
  // };

  // const handleMinus = () => {
  //   setValue((prevValue) => prevValue - 1);
  // };

  // const handleGreen = () => {
  //   setColor(() => "green");
  // };

  // const handleBlue = () => {
  //   setColor(() => "blue");
  // };

  // const handleRed = () => {
  //   setColor(() => "red");
  // };

  // const [state, setState] = useState({ value: 0, color: "red" });

  // const reducerPlusState = () => {
  //   const action = { type: "PLUS", amount: 1 };
  //   setState((prevState) => {
  //     return reducer(action, prevState);
  //   });
  // };

  // const reducerMinusState = () => {
  //   const action = { type: "PLUS", amount: -1 };
  //   setState((prevState) => {
  //     return reducer(action, prevState);
  //   });
  // };

  // const reducerGreenState = () => {
  //   const action = { type: "CHANGE_COLOR", color: "green" };
  //   setState((prevState) => {
  //     return reducer(action, prevState);
  //   });
  // };

  // const reducerBlueState = () => {
  //   const action = { type: "CHANGE_COLOR", color: "blue" };
  //   setState((prevState) => {
  //     return reducer(action, prevState);
  //   });
  // };

  // const reducerRedState = () => {
  //   const action = { type: "CHANGE_COLOR", color: "red" };
  //   setState((prevState) => {
  //     return reducer(action, prevState);
  //   });
  // };

  // const newPlusState = () => {
  //   setState((prevState) => ({ ...prevState, value: prevState.value + 1 }));
  // };

  // const newMinusState = () => {
  //   setState((prevState) => ({ ...prevState, value: prevState.value - 1 }));
  // };

  // const newGreenState = () => {
  //   setState((prevState) => ({
  //     ...prevState,
  //     color: "green",
  //   }));
  // };

  // const newBlueState = () => {
  //   setState((prevState) => ({
  //     ...prevState,
  //     color: "blue",
  //   }));
  // };

  // const newRedState = () => {
  //   setState((prevState) => ({
  //     ...prevState,
  //     color: "red",
  //   }));
  // };

  // 보여지는 것들을 정의
  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: state.color }}>
        {state.value}
      </div>
      <hr />
      {/* <button onClick={() => setValue(value + 1)}>+</button>
      <button onClick={() => setValue(value - 1)}>-</button> */}
      {/* <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button> */}
      {/* <button onClick={newPlusState}>+</button>
      <button onClick={newMinusState}>-</button> */}
      {/* <button onClick={reducerPlusState}>+</button>
      <button onClick={reducerMinusState}>-</button> */}
      <button onClick={() => dispatch({ type: "PLUS", amount: 1 })}>+</button>
      <button onClick={() => dispatch({ type: "MINUS", amount: 1 })}>-</button>
      <button
        onClick={() => dispatch({ type: "CHANGE_COLOR", color: "green" })}
      >
        그린
      </button>
      <button onClick={() => dispatch({ type: "CHANGE_COLOR", color: "blue" })}>
        블루
      </button>
      <button onClick={() => dispatch({ type: "CHANGE_COLOR", color: "red" })}>
        레드
      </button>
      {/* <button onClick={() => setColor("red")}>red</button>
      <button onClick={() => setColor("green")}>green</button>
      <button onClick={() => setColor("blue")}>blue</button> */}
      {/* <button onClick={handleGreen}>green</button>
      <button onClick={handleBlue}>blue</button>
      <button onClick={handleRed}>red</button> */}
      {/* <button onClick={newGreenState}>green</button>
      <button onClick={newBlueState}>blue</button>
      <button onClick={newRedState}>red</button> */}
      {/* <button onClick={reducerGreenState}>green</button>
      <button onClick={reducerBlueState}>blue</button>
      <button onClick={reducerRedState}>red</button> */}
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter;
