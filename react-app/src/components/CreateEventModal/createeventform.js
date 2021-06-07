import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router';
import { getDestination } from '../../store/destinations';
import {createEvent} from '../../store/events'
import { getTrips } from '../../store/trips';




function CreateEventForm() {

  const dispatch = useDispatch();
  const trips = useSelector(state => state?.trips)
  const destination = useSelector(state => state?.destinations?.destination)
  const { cityId, destinationName } = useParams()
  const tripsArr = Object.values(trips).filter((trip) => trip.city_id === Number(cityId))
  const [booked, setBooked] = useState("BOOK")
  const [trip_id, setTripId] = useState("")
  
  let custom_destination_id;
  let default_destination_id;
  if(destination.destination.user_id) { 
      custom_destination_id = destination.destination.id
    } else { 
      default_destination_id = destination.destination.id
  }

  useEffect(() => { 
      dispatch(getDestination(destinationName))
      dispatch(getTrips())
  }, [dispatch])


  const handleSubmit = (e) => {
    e.preventDefault();
    setBooked("BOOKED!")
    return dispatch(createEvent(trip_id, default_destination_id, custom_destination_id))
    
  };  


  const roundDate = (date) => { 
      let newDate = date?.split(' ').slice(1,3).reverse().join(' ')
      return newDate
  }


  const tripsSelect = () => { 
      if (tripsArr.length > 0) { 
          return (
            <div className="create-trip-div">
                <label htmlFor="trips"></label>
                <select
                    className="select-trip"
                    name="trips"
                    onChange={(e) => setTripId(e.target.value)}
                    >
                        <option value="">Select a Trip!</option>
                    {tripsArr.map((oneTrip) => ( 
                        <option key={oneTrip.id} value={oneTrip.id}>{oneTrip.name} from {roundDate(oneTrip?.start_date)} to {roundDate(oneTrip?.end_date)}</option>
                    ))}
                </select>
            </div>
          )
      } else { 
          return (
              <div>You have no trips to this location!</div>
          )
      }
  }


  return (
    <>
      <h2 className="modal-title">Which trip do you want to add this event to?</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={(e) => handleSubmit(e)}>
            {tripsSelect()}
            <button disabled={!trip_id} className="modal-button create-trip-btn" type="submit">{booked}</button>
          </form>
      </div>
    </>
  );
}

export default CreateEventForm;