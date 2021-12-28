import PageLotto from "./components/PageLotto";
import ProfileCard from "./components/ProfileCard";
import memberList from "./data/ProfileCard.json";
import { useState } from "react";

function App() {
  const [memberNum, setMemberNum] = useState(memberList[0].name);
  return (
    <>
      {/* <h1>이준수의 리액트</h1>
      <PageLotto /> */}

      {memberList.map((member, index) => {
        if (memberNum === member.name) {
          return (
            <div className={`member${(index % 4) + 1}`}>
              <ProfileCard
                name={member.name}
                role={member.role}
                email={member.email}
                facebook_url={member.facebook_url}
                profileImage={`/profile-images/member${index + 1}.jpg`}
              >
                <nav>
                  {memberList.map((member) => {
                    return (
                      <a
                        className={memberNum === member.name ? "on" : ""}
                        onClick={() => setMemberNum(member.name)}
                      ></a>
                    );
                  })}
                </nav>
              </ProfileCard>
            </div>
          );
        }
      })}
    </>
  );
}

export default App;
