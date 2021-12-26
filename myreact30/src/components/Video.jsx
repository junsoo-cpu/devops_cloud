import React from 'react';
import ReactPlayer from 'react-player';
import { Layout, List } from 'antd';
import { useState } from 'react';

function Video() {
  const video_list = [
    {
      title: '(Playlist) 그녀가 좋아하는 국내 감성힙합 모음집',
      youtube_id: 'https://www.youtube.com/watch?v=7frbAI5p7KA',
      thumbnail_url:
        'https://i.ytimg.com/vi/7frbAI5p7KA/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAOJ-RBpiGQJptG-URGCELILTZEdw',
    },
    {
      title: '썸녀한테 추천해줬던 감성힙합 모음집#1 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩',
      youtube_id: 'https://www.youtube.com/watch?v=1l64R9QYJtk',
      thumbnail_url:
        'https://i.ytimg.com/vi/1l64R9QYJtk/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBNH7ZAy-LbT65qAaASyQnvFIXKFQ',
    },
    {
      title: '[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 썸녀한테 들려주면 반해버릴 감성힙합 모음집',
      youtube_id: 'https://www.youtube.com/watch?v=PLdfp7JDlpY',
      thumbnail_url:
        'https://i.ytimg.com/vi/PLdfp7JDlpY/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDVD2cex_detIL7M-1LtSmrFqR2Uw',
    },
    {
      title: '담배 피던 그녀가 좋아하던 감성힙합 𝙥𝙡𝙖𝙮𝙡𝙞𝙨𝙩',
      youtube_id: 'https://www.youtube.com/watch?v=rs1Wr6ZFV2E',
      thumbnail_url:
        'https://i.ytimg.com/vi/rs1Wr6ZFV2E/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDWkVA4B6ijHgAS4MKDQcPytS7AkA',
    },
    {
      title: '그녀가 좋아하는 외국힙합 모음집 (Playlist)',
      youtube_id: 'https://www.youtube.com/watch?v=H6oqbvhWY4g',
      thumbnail_url:
        'https://i.ytimg.com/vi/H6oqbvhWY4g/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAl99Eu_TAvDjfs6if8ooY8OQLgtQ',
    },
    {
      title: '[Playlist] 그 해 여름, 잊지못할 너와의 추억',
      youtube_id: 'https://www.youtube.com/watch?v=GFGczlLm8cg',
      thumbnail_url:
        'https://i.ytimg.com/vi/GFGczlLm8cg/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCUzE60RIFw5C-Oe179fyoM9c1RJQ',
    },
    {
      title: '[𝙋𝙡𝙖𝙮𝙡𝙞𝙨𝙩] 자기 전, 누워서 그루브 타기 좋은 힙합 모음집',
      youtube_id: 'https://www.youtube.com/watch?v=7frbAI5p7KA',
      thumbnail_url:
        'https://i.ytimg.com/vi/1HRty0Yn8ZQ/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBzq8IyDMacDNxZnzq7del7RchtMw',
    },
  ];
  // TODO: 리스트 형식으로 만들고 클릭 시 그 영상이 보여지도록

  const [youtubeUrl, setYoutubeUrl] = useState('');

  const { Sider, Footer, Content } = Layout;

  return (
    <>
      <Layout>
        <Layout style={{ marginLeft: 200 }}>
          <Content style={{ overflow: 'auto' }}>
            <div style={{ padding: 100 }}>
              <ReactPlayer url={youtubeUrl} />
            </div>
          </Content>
          <Sider
            class="scroller"
            style={{
              overflow: 'auto',
              height: '80vh',
              position: 'fixed',
              right: 0,
              backgroundColor: 'white',
            }}
            width={500}
          >
            <List
              bordered={true}
              itemLayout="horizontal"
              dataSource={video_list}
              renderItem={(video) => (
                <List.Item
                  bordered={true}
                  onClick={() => setYoutubeUrl(video.youtube_id)}
                >
                  <img src={video.thumbnail_url} />
                  <List.Item.Meta title={<h4>{video.title}</h4>} />
                </List.Item>
              )}
            />
          </Sider>
        </Layout>
        <Footer></Footer>
      </Layout>
    </>
  );
}
export default Video;
