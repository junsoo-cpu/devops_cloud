// import profileListData from "./data/post-list.json";
import ProfileCard from "./components/ProfileCard";
import Axios from "axios";

const { useState, useEffect } = require("react");

function App() {
  const [profileList, setProfileList] = useState([]); // 데이터 관련 상태값

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [pageName, setPageName] = useState("진"); // 페이지 네임 지정 상태값
  // App 컴포넌트가 마운트될 때
  // 아래의 함수가 자동 호출됩니다.

  return (
    <div>
      {profileList.map((member, index) => {
        if (pageName == member.name) {
          return (
            <div className={`member${(index % 4) + 1}`}>
              <ProfileCard {...member}>
                <nav>
                  {profileList.map((member) => {
                    return (
                      <a
                        className={pageName === member.name ? "on" : ""}
                        onClick={() => setPageName(member.name)}
                      ></a>
                    );
                  })}
                </nav>
              </ProfileCard>
            </div>
          );
        }
      })}
    </div>
  );
}

export default App;

// import PageLotto from "./components/PageLotto";
// import ProfileCard from "./components/ProfileCard";
// import memberList from "./data/ProfileCard.json";
// import { useState } from "react";

// function App() {
//   const [memberNum, setMemberNum] = useState(memberList[0].name);
//   return (
//     <>
//       {/* <h1>이준수의 리액트</h1>
//       <PageLotto /> */}

//       {memberList.map((member, index) => {
//         if (memberNum === member.name) {
//           return (
//             <div className={`member${(index % 4) + 1}`}>
//               <ProfileCard
//                 name={member.name}
//                 role={member.role}
//                 email={member.email}
//                 facebook_url={member.facebook_url}
//                 profileImage={`/profile-images/member${index + 1}.jpg`}
//               >
//                 <nav>
//                   {memberList.map((member) => {
//                     return (
//                       <a
//                         className={memberNum === member.name ? "on" : ""}
//                         onClick={() => setMemberNum(member.name)}
//                       ></a>
//                     );
//                   })}
//                 </nav>
//               </ProfileCard>
//             </div>
//           );
//         }
//       })}
//     </>
//   );
// }

// export default App;
