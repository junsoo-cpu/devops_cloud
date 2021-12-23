import { Input } from 'antd';
import { useState } from 'react';

function MelonSearch() {
  const [query, setQuery] = useState('');

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
    console.log(`검색어 ${query}(으)로 검색`);
    console.groupEnd();
  };

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      멜론 검색
      <hr />
      검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요"
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
    </div>
  );
}

export default MelonSearch;
