import { useState } from "react";

const makeLottoNumbers = () => {
  const lottoNum = [];
  while (lottoNum.length < 7) {
    const number = parseInt(Math.random() * 45) + 1;
    if (lottoNum.indexOf(number) < 0) {
      lottoNum.push(number);
    }
  }
  lottoNum.sort((a, b) => {
    return a - b;
  });
  return lottoNum;
};

function PageLotto() {
  const [numbers, setNumbers] = useState([]);

  const handleClick = () => {
    setNumbers(makeLottoNumbers());
  };

  return (
    <div>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지</button>
      {numbers.map((number) => {
        return <div style={style}>{number}</div>;
      })}
    </div>
  );
}

const style = {
  display: "inline-block",
  fontSize: "2rem",
  margin: "1rem",
};

export default PageLotto;
