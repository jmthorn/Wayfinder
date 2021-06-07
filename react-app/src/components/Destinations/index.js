import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route, NavLink, useHistory } from 'react-router-dom';
import {deleteDestination, getDestinations} from '../../store/destinations'
import Destination_Detail from '../Destination_Detail'
import CreateDestinationModal from '../CreateDestinationModal'
import './destinations.css'

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  const destinations = useSelector(state => state.destinations.destinations)
  const { cityId, destinationName } = useParams()
//   const destination_name = destinationName.split("_").join(" ")
  const history = useHistory()


  useEffect(() => { 
    if (destinations && !destinationName) { 
        history.push(`/destinations/${cityId}/${destinations.default_destinations[0].name.split("_").join(" ")}`)
    }
  }, [dispatch,destinationName, destinations, cityId])

  useEffect(() => { 
      dispatch(getDestinations(cityId))
  }, [dispatch])


  const removeDestination = (destinationId) => { 
    dispatch(deleteDestination(destinationId))
  }

  return (
    <div id="destinations-page-container">
        <nav id="destination-nav">
            {destinations?.default_destinations?.map((destination) =>  (
                <NavLink key={destination.name} to={`/destinations/${cityId}/${destination.name.split(" ").join("_")}`}>
                    <div className="destination">{destination.name}</div>
                    <div className="dest-nav-line"></div>
                </NavLink>
            ))}
            {destinations?.custom_destinations?.map((destination) =>  (
                <NavLink key={destination.name} to={`/destinations/${cityId}/${destination.name.split(" ").join("_")}`}>
                    <div className="custom-destination-info-container">
                        <div className="destination">{destination.name}</div>
                        <button value={destination.id} onClick={(e) => removeDestination(e.target.value)} className="delete-destination">-</button> 
                    </div>
                    <div className="dest-nav-line"></div>

                </NavLink>
            ))}
            <div id="add-dest">
                <div>Add Destination</div>
                <CreateDestinationModal cityId={cityId}/>
                {/* <button  id="add-dest-button">+</button> */}
            </div>
        </nav>
        <Route path="/destinations/:cityId/:destinationName">
            <Destination_Detail />
        </Route>
    </div>
  );
}

export default Destinations;