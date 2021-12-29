import { useState } from 'react';

function PageProfile() {
  const [profileList] = useState([
    // {
    //   uniqueId: 'bts-jin',
    //   name: '진',
    //   role: '서브보컬',
    //   mbti: 'INFP',
    //   instagramUrl: 'https://instagram.com/jin',
    //   profileImageUrl:
    //     'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
    // },
  ]);

  return (
    <div>
      <h2>PageProfile</h2>
      {profileList.length === 0 && <h3>등록 된 프로필이 없습니다.</h3>}
      {profileList.map((member) => {
        return (
          <div>
            <h4>{member.name}</h4>
            <ul>
              <li>{member.role}</li>
              <li>{member.mbti}</li>
              <li>{member.instagramUrl}</li>
              <img
                src={member.profileImageUrl}
                style={{ maxWidth: '100%' }}
                alt=""
              />
            </ul>
          </div>
        );
      })}
    </div>
  );
}

export default PageProfile;
