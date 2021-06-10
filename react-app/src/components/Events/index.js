import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route, NavLink, useHistory } from 'react-router-dom';
import Itinerary from '../Itinerary'
import {removeEvent, getEvents} from '../../store/events'
import './events.css'
import { getTrips } from '../../store/trips';
import { getCities } from '../../store/cities';

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities?.cities)
  const destinations = useSelector(state => state.destinations.destinations)
  const events = useSelector(state => state.events)
  const trips = useSelector(state => state?.trips)
  const tripsArr = Object.values(trips)
  const eventsArr = Object.values(events)
  const { trip_id } = useParams()
  const chosenTrip = tripsArr.filter((trip) => trip.id === Number(trip_id))
  const history = useHistory()

  useEffect(() => { 
      dispatch(getEvents(trip_id))
      dispatch(getTrips())
      dispatch(getCities())
  }, [dispatch])


  const deleteEvent = (event_id) => { 
    dispatch(removeEvent(event_id))
  }

  return (
    <div id="events-page-container">
        <nav id="events-nav">
            {eventsArr.map((event) =>  (
                // <NavLink key={event.name} to={`/destinations/${cityId}/${event.name.split(" ").join("_")}`}>
                <div key={event.id}>
                    <div className="event-info-container">
                        <div className="event">{event.name}</div>
                        <button value={event.id} onClick={(e) => deleteEvent(e.target.value)} className="delete-event">-</button> 
                    </div>
                    <div className="event-nav-line"></div>
                </div>
                // </NavLink>
            ))}
            {!eventsArr.length &&  (
                <div id="no-events">You have no events!</div>
            )}
            <div id="add-event">
                <div>Add Destinations</div>
                {chosenTrip && <button  onClick={() => history.push(`/destinations/${chosenTrip[0]?.city_id}`)} id="add-event-button">+</button>}
            </div>
        </nav>

        <Itinerary />
    </div>
  );
}

export default Destinations;