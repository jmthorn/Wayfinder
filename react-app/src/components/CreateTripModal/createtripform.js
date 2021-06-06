import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {createTrip} from '../../store/trips'
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";



function CreateTripForm({cityId}) {

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [booked, setBooked] = useState("BOOK")
  const cities = useSelector(state => state.cities.cities)
  const chosenCity = cities.cities.filter((city) => city.id === cityId)[0]
  const chosenCityId = chosenCity.id
  const dispatch = useDispatch();
  const [error, setError] = useState("");


  const handleSubmit = (e) => {
    e.preventDefault();
    if(endDate < startDate) { 
      setError("Your end date is before your start date!")
    } else {
      setBooked("BOOKED!")
      return dispatch(createTrip(chosenCityId, startDate, endDate))
    }
  };  


  return (
    <>
      <h2 className="modal-title">Create a Trip</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={(e) => handleSubmit(e)}>
              <label>When are you going to {chosenCity.name}?
                {error && (
                  <div className="modal-error">{error}</div>
                )}
                <div className="modal-date-inputs">
                    <DatePicker selected={startDate} placeholderText="Start Date" onChange={(date) => setStartDate(date)} />
                    <div className="modal-to">to</div>
                    <DatePicker selected={endDate} placeholderText="End Date" onChange={(date) => setEndDate(date)} />
                </div>
              </label>
              <button className="modal-button" type="submit">{booked}</button>
          </form>
      </div>
    </>
  );
}

export default CreateTripForm;