function ReviewForm({ fieldValues, handleChange, handleSubmit, handleButton }) {
  return (
    <div className="border-2 border-gray-300 p-3">
      <h2>평점</h2>
      <select onChange={handleChange} name="number" value={fieldValues.number}>
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
      </select>
      <hr />
      <label
        for="exampleFormControlTextarea1"
        class="form-label inline-block mb-2 text-gray-700"
      >
        리뷰
      </label>
      <textarea
        cols="47"
        rows="5"
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        name="content"
        value={fieldValues.content}
      />
      <hr />
      <button
        className="m-1 p-1 border-2 border-blue-500 p-3 rounded-lg review--list"
        style={{ background: 'skyblue' }}
        onClick={() => {
          handleSubmit();
          handleButton({ logged: true });
        }}
      >
        저장
      </button>
    </div>
  );
}
export default ReviewForm;
