import PageLotto from "./components/PageLotto";
import ProfileCard from "./components/ProfileCard";
import ProfileImage1 from "./components/ProfileImage/member1.jpg";
import ProfileImage2 from "./components/ProfileImage/member2.jpg";
import ProfileImage3 from "./components/ProfileImage/member3.jpg";
import ProfileImage4 from "./components/ProfileImage/member4.jpg";

import { useState } from "react";

function App() {
  const [pageName, setPageName] = useState("member1");
  return (
    <>
      <h1>이준수의 리액트</h1>
      <PageLotto />
      <nav className="others">
        {pageName === "member1" && (
          <ProfileCard
            profileImage={ProfileImage1}
            name="Anna"
            role="student"
            facebook_url="Visit My Facebook page."
            email="Annn1133@naver.com"
            className="on"
            changePageName={setPageName}
          />
        )}
        {pageName === "member2" && (
          <ProfileCard
            profileImage={ProfileImage2}
            name="Alice"
            role="police"
            facebook_url="Visit My Facebook page."
            email="buww11@naver.com"
            className="on"
            changePageName={setPageName}
          />
        )}
        {pageName === "member3" && (
          <ProfileCard
            profileImage={ProfileImage3}
            name="Dred"
            role="student"
            facebook_url="Visit My Facebook page."
            email="hello22@naver.com"
            className="on"
            changePageName={setPageName}
          />
        )}
        {pageName === "member4" && (
          <ProfileCard
            profileImage={ProfileImage4}
            name="Davis"
            role="teacher"
            facebook_url="Visit My Facebook page."
            email="hadaboni20@naver.com"
            className="on"
            changePageName={setPageName}
          />
        )}
      </nav>
    </>
  );
}

export default App;
