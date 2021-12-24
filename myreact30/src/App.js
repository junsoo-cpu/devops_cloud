import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import TopNav from 'components/TopNav';

import { useState } from 'react';

function App() {
  const [pageName, setPageName] = useState('about');

  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };

  return (
    <>
      <h1>이준수의 리액트</h1>
      {/* <button onClick={changePageName}>페이지 토글</button> */}
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
    </>
  );
}

export default App;
