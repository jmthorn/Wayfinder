import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {updateTrip} from '../../store/trips'
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
  const [error, setError] = useState("");


  const handleSubmit = (e) => {
    e.preventDefault();
    if(endDate < startDate) { 
      setError("Your end date is before your start date!")
    } else {
      setUpdate("UPDATED!")
      return dispatch(updateTrip(chosenTripId, startDate, endDate))
    }
  };  


  const cancelTrip = (e) => {
    e.preventDefault();
    setUpdate("CANCELED!")
    return dispatch(cancelTrip(chosenTripId))
    
  };  


  return (
    <>
      <h2 className="modal-title">Update your Trip</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={(e) => handleSubmit(e)}>
              <label>When are you going to {chosenTrip.name}?
                {error && (
                  <div className="modal-error">{error}</div>
                )}
                <div className="modal-date-inputs">
                    <DatePicker selected={startDate} placeholderText="Start Date" onChange={(date) => setStartDate(date)} />
                    <div className="modal-to">to</div>
                    <DatePicker selected={endDate} placeholderText="End Date" onChange={(date) => setEndDate(date)} />
                </div>
              </label>
              <button className="modal-button" type="submit">{update}</button>
              <button  className="modal-button modal-button-cancel" onClick={() => cancelTrip}>{cancel}</button>
          </form>
      </div>
    </>
  );
}

export default UpdateTripForm;