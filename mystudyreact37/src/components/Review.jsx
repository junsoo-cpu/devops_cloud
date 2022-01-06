import './Review.css';
import Star from './Star';
function Review({ review }) {
  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-green-500 border-2 hover:scale-105 cursor-pointer `}
    >
      {review.content}
      <Star score={review.number} />
    </div>
  );
}
export default Review;
