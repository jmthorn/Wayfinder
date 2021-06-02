import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route, NavLink } from 'react-router-dom';
import {getDestinations} from '../../store/destinations'
import Destination_Detail from '../Destination_Detail'
import './destinations.css'

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  const destinations = useSelector(state => state.destinations.destinations)
  const { cityId } = useParams()

  console.log(destinations)

  useEffect(() => { 
      dispatch(getDestinations(cityId))
  }, [dispatch])

//   let default_destinations_div = []
//   let custom_destinations_div = []

  return (
    <div id="destinations-page-container">
        <nav>
            {destinations?.default_destinations?.map((destination) =>  (
                <NavLink key={destination.name} to={`/destinations/${cityId}/${destination.name.split(" ").join("-")}`}>
                    <div>{destination.name}</div>
                </NavLink>
            ))}
            {destinations?.custom_destinations?.map((destination) =>  (
                <NavLink key={destination.name} to={`/destinations/${cityId}/${destination.name.split(" ").join("-")}`}>
                    <div>{destination.name}</div>
                </NavLink>
            ))}
        </nav>
        <Route path="/destinations/:cityId/:destinationName">
            <Destination_Detail />
        </Route>
    </div>
  );
}

export default Destinations;