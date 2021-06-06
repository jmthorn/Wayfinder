import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router';
import { getDestination } from '../../store/destinations';
import {createEvent} from '../../store/events'




function CreateEventForm() {

  const dispatch = useDispatch();
  const [booked, setBooked] = useState("BOOK")
  const destination = useSelector(state => state?.destinations?.destination)
  const { cityId, destinationName } = useParams()
  const [error, setError] = useState("");
  let trip_id;
  let default_destination_id = null;
  let custom_destination_id = null;
  
  if(destination.destination.user_id) { 
      custom_destination_id = destination.destination.id
  } else { 
      default_destination_id = destination.destination.id
  }


  useEffect(() => { 
      dispatch(getDestination(destinationName))

  }, [dispatch])


  const handleSubmit = (e) => {
    e.preventDefault();

    setBooked("BOOKED!")
    
    return dispatch(createEvent(trip_id, default_destination_id, custom_destination_id))
    
  };  


  return (
    <>

    </>
  );
}

export default CreateEventForm;