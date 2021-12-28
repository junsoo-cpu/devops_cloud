import PageLotto from "./components/PageLotto";
import ProfileCard from "./components/ProfileCard";
import memberList from "./data/ProfileCard.json";
import { useState } from "react";

function App() {
  const [memberNum, setMemberNum] = useState("Anna");
  return (
    <>
      {/* <h1>이준수의 리액트</h1>
      <PageLotto /> */}

      {memberList.map((member, index) => {
        if (memberNum === member.name) {
          return (
            <div className={`member${index}`}>
              <ProfileCard
                name={member.name}
                role={member.role}
                email={member.email}
                facebook_url={member.facebook_url}
                changePageName={setMemberNum}
              />
            </div>
          );
        }
      })}
    </>
  );
}

export default App;
