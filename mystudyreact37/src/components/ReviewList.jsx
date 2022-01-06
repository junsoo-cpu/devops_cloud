import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import ReviewForm from './ReviewForm';
import './ReviewList.css';
import Review from './Review';

const INITIAL_STATE = [
  { id: 1, content: '재미있는 영화', number: 5 },
  { id: 2, content: '반전의 연속', number: 4 },
  { id: 3, content: '두번 보고 싶은 영화', number: 5 },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues, setFieldValues] =
    useFieldValues({
      content: '',
      number: 0,
    });

  const appendReview = () => {
    const { id: reviewId } = fieldValues;

    // 새로운 리뷰 저장
    if (!reviewId) {
      reviewId = new Date().getTime();
      const createdReview = { ...fieldValues, id: reviewId };
      setReviewList((prevReviewList) => [...prevReviewList, createdReview]);
      clearFieldValues();
    }
    // 기존 리뷰 수정
    else {
      const editedReview = { ...fieldValues };
      setReviewList((prevReviewList) =>
        prevReviewList.map((review) => {
          if (review.id === editedReview.id) return editedReview;
          return review;
        }),
      );
    }
  };

  const willEditReview = (editingReview) => {
    setFieldValues(editingReview);
    handleButton();
  };

  const deleteReview = (deletingReview) => {
    setReviewList((prevReviewList) =>
      // prevReviewList.filter((review) => review.id !== deletingReview.id),
      prevReviewList.filter(
        ({ id: reviewId }) => reviewId !== deletingReview.id,
      ),
    );
    return true;
    // TODO : reviewList 배열 상탯값에서 deletingReview에 해당하는 리뷰를 제거
  };

  const [reviewButton, setReviewButton] = useState('a');
  const handleButton = () => {
    setReviewButton(() => {
      if (reviewButton === 'a') {
        return 'b';
      } else if (reviewButton === 'b') {
        return 'a';
      }
      return reviewButton;
    });
  };

  return (
    <div className="review-list">
      <h2 className="m-3 p-1 text-xl border-b-2 border-red-400">Review List</h2>
      {reviewButton === 'a' && (
        <button
          className="m-1 p-1 border-2 border-yellow-500 p-3 rounded-lg review-list"
          onClick={handleButton}
        >
          리뷰쓰기
        </button>
      )}
      {reviewButton === 'b' && (
        <label className="block text-center">
          <ReviewForm
            fieldValues={fieldValues}
            handleChange={handleChange}
            handleSubmit={appendReview}
            handleButton={handleButton}
          />
        </label>
      )}

      {reviewList.map((review) => (
        <Review
          key={review.id}
          review={review}
          handleEdit={() => willEditReview(review)}
          handleDelete={() => deleteReview(review)}
        />
      ))}
    </div>
  );
}

export default ReviewList;
