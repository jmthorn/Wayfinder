// frontend/src/components/LoginFormModal/index.js
import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';



function CreateTripForm({cityId}) {

  const cities = useSelector(state => state.cities.cities)
  const chosenCity = cities.cities.filter((city) => city.id === cityId)
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    setErrors([]);
    return dispatch().catch(
      async (res) => {
        const data = await res.json();
        if (data && data.errors) setErrors(data.errors);
      }
    );
  };  


  return (
    <>
      <h2 className="modal-title">Create a Trip</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={handleSubmit}>
              <label for="">When are you going to {chosenCity[0].name}?
                <div className="modal-date-inputs">
                    <input placeholder="Start Date"></input>
                    <input placeholder="End Date"></input>
                </div>
              </label>
              <button type="submit">BOOK</button>
          </form>
      </div>
    </>
  );
}

export default CreateTripForm;