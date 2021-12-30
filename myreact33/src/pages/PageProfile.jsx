import { useState, useEffect } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [error, setError] = useState(null);

  const handleRefresh = () => {
    setError(null);
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const newProfileList = response.data.map((profile) => ({
          ...profile,
          instagramUrl: profile.instagram_url,
          profileImageUrl: profile.profile_image_url,
        }));

        setProfileList(newProfileList);
      })
      .catch((error) => {
        setError(error);
      });
  };

  const handleClear = () => {
    return setProfileList([]);
  };

  useEffect(() => {
    handleRefresh();
  }, []);

  return (
    <div>
      <h2>PageProfile</h2>
      <button onClick={handleClear}> 클리어 </button>
      <button onClick={handleRefresh}> 새로고침 </button>
      {profileList.length === 0 && <h3>등록 된 프로필이 없습니다.</h3>}
      {error && <h5>조회 시 에러가 발생했습니다.</h5>}
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
