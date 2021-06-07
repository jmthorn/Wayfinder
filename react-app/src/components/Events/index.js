import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, Route, NavLink } from 'react-router-dom';
import Itinerary from '../Itinerary'
import {removeEvent, getEvents} from '../../store/events'
import './events.css'

const Destinations = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  const destinations = useSelector(state => state.destinations.destinations)
  const events = useSelector(state => state.events)
  const eventsArr = Object.values(events)
  const { trip_id } = useParams()

  useEffect(() => { 
      dispatch(getEvents(trip_id))
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
        </nav>
        {/* <Route path="/events/itinerary/:tripId"> */}
        <Itinerary />
        {/* </Route> */}
    </div>
  );
}

export default Destinations;