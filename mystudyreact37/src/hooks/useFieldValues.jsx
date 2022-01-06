import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const clearFieldValues = () => setFieldValues(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    // setter에 값 지정
    // setFieldValues({
    //   ...fieldValues,
    //   [name]: value,
    // });

    // setter에 함수 지정
    setFieldValues((prevFieldValues) => {
      return {
        ...prevFieldValues,
        [name]: value,
      };
    });
  };

  return [fieldValues, handleChange, clearFieldValues, setFieldValues];
}

export default useFieldValues;
