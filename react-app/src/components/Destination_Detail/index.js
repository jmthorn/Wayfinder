import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route } from 'react-router-dom';
import './destination_detail.css'

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  const destinations = useSelector(state => state.cities.destinations)
  const { destinationId } = useParams()

  useEffect(() => { 
    //   dispatch(getDestination(destinationId))
  }, [dispatch])

  return (
    <div id="destinations-detail-container">
        <div>DEFAULT</div>
    </div>
  );
}

export default Destinations;