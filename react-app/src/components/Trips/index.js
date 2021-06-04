import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import {getCities} from '../../store/cities'
import {getTrips} from '../../store/trips'
import UpdateTripModal from '../UpdateTripModal';
import './trips.css'

const Trips = () => {

  const dispatch = useDispatch()
  const trips = useSelector(state => state?.trips)

  
  const tripsarr = Object.values(trips)

  useEffect(() => { 
      dispatch(getTrips())
  }, [dispatch])


  const roundDate = (date) => { 
      let newDate = date?.split(' ').slice(1,3).reverse().join(' ')
      return newDate
  }

  return (
    <div id="trips-page-container">
        <h1>YOUR TRIPS</h1>
        <p>Edit, delete or explore your trips</p>
        <div className="trips-line"></div>
        <h3>All Trips</h3>
        <div className="trips-line"></div>
        <div id="trips-container">
            {tripsarr?.map((trip) => ( 
                <div key={trip?.id} className="trip-container">
                    <Link to={`/mytrips/${trip?.id}`}>
                        <div className="trip-image-container">
                            <div className="trip-image-info">
                                <div className="trip-start-end">{roundDate(trip?.start_date)} - {roundDate(trip?.end_date)}</div>
                                <button className="itinerary-button">ITINERARY</button>
                            </div>
                            <img src={trip?.image_url} alt="trip_image"></img>
                        </div>
                    </Link>
                    <div className="trip-info">
                        <div className="trip-name">
                            <div >{trip?.name}</div>
                            <div className="trip-line"></div>
                        </div>
                        <UpdateTripModal tripId={trip?.id}/>                    
                        </div>
                </div>
            ))}
        </div>
    </div>
  );
}

export default Trips;