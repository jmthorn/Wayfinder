import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {updateTrip, deleteTrip} from '../../store/trips'
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";



function UpdateTripForm({tripId}) {

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [update, setUpdate] = useState("UPDATE TRIP")
  const [cancel, setCancel] = useState("CANCEL TRIP")
//   const cities = useSelector(state => state.cities.cities)
  const trips = useSelector(state => state.trips)
  const tripsarr = Object.values(trips)
  const chosenTrip = tripsarr.filter((trip) => trip?.id === tripId)[0]
  const chosenTripId = chosenTrip.id
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);


  const handleSubmit = (e) => {
    e.preventDefault();
    let new_errors = []
    if(endDate < startDate) { 
      new_errors.push("Your end date is before your start date!")
    } else if (!endDate || !startDate) { 
      new_errors.push("You're missing a date!")
    }
    setErrors(new_errors)
    console.log(errors)
    if (!errors) {
      setUpdate("UPDATED!")
      return dispatch(updateTrip(chosenTripId, startDate, endDate))
    }
  };  


  const cancelTrip = (e) => {
    e.preventDefault();
    setCancel("CANCELED!")
    return dispatch(deleteTrip(chosenTripId))
    
  };  


  return (
    <>
      <h2 className="modal-title">Update your Trip</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form >
              <label>When are you going to {chosenTrip.name}?
                {errors && errors?.map((error) => (
                    <div className="modal-error">{error}</div>
                  )
                )}
                <div className="modal-date-inputs">
                    <DatePicker selected={startDate} placeholderText="Start Date" onChange={(date) => setStartDate(date)} />
                    <div className="modal-to">to</div>
                    <DatePicker selected={endDate} placeholderText="End Date" onChange={(date) => setEndDate(date)} />
                </div>
              </label>
              <button className="modal-button" type="submit" onClick={(e) => handleSubmit(e)}>{update}</button>
              <button  className="modal-button modal-button-cancel" onClick={(e) => cancelTrip(e)}>{cancel}</button>
          </form>
      </div>
    </>
  );
}

export default UpdateTripForm;