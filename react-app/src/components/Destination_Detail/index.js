import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route } from 'react-router-dom';
import {getDestination, getDestinations} from '../../store/destinations'
import CreateEventModal from '../CreateEventModal';
import UpdateDestinationsModal from '../UpdateDestinationsModal'
import GoogleApiWrapper from '../GoogleMapsAPI';

import './destination_detail.css'

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  const destination = useSelector(state => state?.destinations?.destination)
  const { cityId, destinationName } = useParams()
  const destination_name = destinationName.split("_").join(" ")
  const [apiKey, setApiKey] = useState('');


  useEffect(() => {
  (async()=> {
    const res = await fetch('/api/retrieve_api/');
    const { apiKey } = await res.json();
    setApiKey(apiKey);
    })()
  })

  
  useEffect(() => { 
      dispatch(getDestination(destinationName))

  }, [dispatch, cityId, destinationName])

  
  return (
    <div id="destinations-detail-container">
        <div id="destination-image">
          <img src={destination?.destination?.image_url}></img>
        </div>
        <div id="destination-info">
          <div id="dest-header-container">
            <div id="dest-name">{destination?.destination?.name}</div>
            <CreateEventModal cityId={cityId}/>
          </div>
          <div id="dest-line"></div>
          <div id="dest-address">{destination?.destination?.address}</div>
          <div id="dest-desc">{destination?.destination?.description}</div>
          <div id="dest-dur">Duration: {Math.round(((destination?.destination?.duration)/60)*100)/100} Hrs.</div>
          {destination?.destination?.user_id && (
            <UpdateDestinationsModal destination={destination?.destination}/>
          )}
          <div className="maps-container">
            {destination?.destination && <GoogleApiWrapper apiKey={apiKey} coordinate={{lat:destination?.destination?.lat,lng:destination?.destination?.lng}}/>}
          </div>
        </div>
    </div>
  );
}

export default Destinations;