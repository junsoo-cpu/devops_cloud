import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import PageLotto from 'pages/PageLotto';
import TopNav from 'components/TopNav';
import PageVideo from 'pages/PageVideo';

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
      {pageName === 'lotto' && <PageLotto />}
      {pageName === 'video' && <PageVideo />}
    </>
  );
}

export default App;
