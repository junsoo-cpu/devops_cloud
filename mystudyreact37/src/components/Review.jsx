import './Review.css';
import Star from './Star';
import { useState } from 'react';

// review : 보여줄 리뷰 목록
// handleEdit : 인자없는 함수, 수정 버튼 클릭 시에 호출
// handleDelete : 인자 없는 함수, 삭제 버튼 클릭 시에 호출

function Review({ review, handleEdit, handleDelete }) {
  const [showMenu, setShowMenu] = useState(false);

  const handleClickedEditButton = () => {
    if (handleEdit) {
      handleEdit();
    } else {
      console.warn('[Review] handleEdit 속성값이 지정되지 않았습니다.');
    }
  };

  const handleClickedDeleteButton = () => {
    if (handleDelete) {
      handleDelete();
    } else {
      console.warn('[Review] handleDelete 속성값이 지정되지 않았습니다.');
    }
  };

  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className={`m-1 p-1 pt-3 rounded-lg  border-green-500 border-2 hover:scale-105 relative`}
    >
      {showMenu && (
        <div className="text-xs absolute top-0 right-0">
          <span
            onClick={handleClickedEditButton}
            className="text-blue-700 hover:text-blue-300 cursor-pointer mr-2"
          >
            수정
          </span>
          <span
            onClick={handleClickedDeleteButton}
            className="text-red-700 hover:text-red-300 cursor-pointer"
          >
            삭제
          </span>
        </div>
      )}

      {review.content}
      <Star score={review.number} />
    </div>
  );
}
export default Review;
