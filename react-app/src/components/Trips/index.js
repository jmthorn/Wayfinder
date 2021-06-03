import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import {getCities} from '../../store/cities'
import {getTrips} from '../../store/trips'
// import UpdateTripModal from '../UpdateTripModal';
import './trips.css'

const Trips = () => {

  const dispatch = useDispatch()
  const trips = useSelector(state => state.trips.trips)

  console.log(trips)
//   console.log(trips[0].cities.image_url)

  useEffect(() => { 
      dispatch(getTrips())
  }, [dispatch])


  return (
    <div id="trips-page-container">
        <h1>THE TRIPS</h1>
        <p>Edit, delete or explore your trips</p>
        <div className="trips-line"></div>
        <h3>All Trips</h3>
        <div className="trips-line"></div>
        <div id="trips-container">
            {/* {trips?.trips.map((trip) => ( 
                <div key={trip.id} className="trip-container">
                    <Link to={`/destinations/${city.id}`}>
                        <div className="city-image-container">
                            <img src={city.image_url} alt="city_image"></img>
                        </div>
                    </Link>
                    <div className="trip-info">
                        <div className="trip-name">
                            <div >{city.name}</div>
                            <div className="trip-line"></div>
                        </div>
                        <UpdateTripModal cityId={city.id}/>                    
                        </div>
                </div>
            ))} */}
        </div>
    </div>
  );
}

export default Trips;