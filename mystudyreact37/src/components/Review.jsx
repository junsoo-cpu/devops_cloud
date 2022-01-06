import './Review.css';
import Star from './Star';
import { useState } from 'react';

function Review({ review }) {
  const [showMenu, setShowMenu] = useState(false);
  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className={`m-1 p-1 pt-3 rounded-lg  border-green-500 border-2 hover:scale-105 relative`}
    >
      {showMenu && (
        <div className="text-xs absolute top-0 right-0">
          <span className="text-blue-700 hover:text-blue-300 cursor-pointer mr-2">
            수정
          </span>
          <span className="text-red-700 hover:text-red-300 cursor-pointer">
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
