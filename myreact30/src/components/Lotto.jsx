import { useState } from 'react';
import Ball from './Ball';

function Lotto() {
  //6개로 값이 나열될것이기 때문에 배열처리 - 값은 담지 않음

  const [value, setValue] = useState([]);

  const lottoNum = () => {
    let lotto = [];
    while (lotto.length < 7) {
      let number = parseInt(Math.random() * 45) + 1;
      if (lotto.indexOf(number) < 0) {
        lotto.push(number);
      }
    }
    lotto.sort((a, b) => {
      return a - b;
    });
    return lotto;
  };

  const createNumber = () => {
    setValue(lottoNum);
  };

  return (
    <div>
      <button onClick={createNumber}>로또</button>
      {value.map((number) => (
        <Ball number={number} />
      ))}
    </div>
  );
}

export default Lotto;
