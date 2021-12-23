import { Input } from 'antd';
import { useState } from 'react';

import { List, Avatar } from 'antd';

import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';

import { Button, Tooltip } from 'antd';
import { SearchOutlined } from '@ant-design/icons';

function MelonSearch() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };

  const handlePressEnter = (e) => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}(으)로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        // ALBUMCONTENTS, ARTISTCONTENTS
        const {
          data: { SONGCONTENTS: searchedSongList },
        } = response;
        console.group('멜론 검색결과');
        console.log(response);

        setSongList(searchedSongList);

        console.groupEnd();
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.log(error);
        console.groupEnd();
      });
  };

  const data = [
    {
      title: 'Ant Design Title 1',
    },
  ];

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어 : {query}
      <Tooltip title="search">
        <Button
          shape="circle"
          icon={<SearchOutlined />}
          onClick={handlePressEnter}
        />
      </Tooltip>
      <br />
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      {songList.map((song) => {
        return (
          <List
            itemLayout="horizontal"
            dataSource={data}
            renderItem={() => (
              <List.Item>
                <List.Item.Meta
                  avatar={<Avatar src={song.ALBUMIMG} />}
                  title={song.SONGNAME}
                  description={song.ARTISTNAME}
                />
              </List.Item>
            )}
          />
        );
      })}
    </div>
  );
}

export default MelonSearch;
