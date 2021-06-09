import React, { useEffect, useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar'
// import { DragDropContext } from "react-dnd";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import moment from 'moment'
import { useDispatch, useSelector } from 'react-redux';
import { getEvents, updateEvent } from '../../store/events';
import { useParams } from 'react-router';
import "react-big-calendar/lib/css/react-big-calendar.css"
import { getTrips } from '../../store/trips';
import './itinerary.css'


const Itinerary = () => {

  const events = useSelector(state => state.events)
  const trips = useSelector(state => state.trips)
  const { trip_id } = useParams()
  const chosenTrip = Object.values(trips).filter((trip) => trip.id === Number(trip_id))
  const eventsArr = Object.values(events)
  const localizer = momentLocalizer(moment)
  const DnDCalendar = withDragAndDrop(Calendar);
  const dispatch = useDispatch()
  const today = new Date(); 
  const tripStartDate = new Date(chosenTrip[0]?.start_date) 
  const tripEndDate = new Date(chosenTrip[0]?.end_date) 
  const [startDate, setDate] = useState("")


  useEffect(() => { 
    if (chosenTrip.length) { 
      setDate(new Date(chosenTrip[0].start_date))
    }
  }, [chosenTrip.length])

  useEffect(() => { 
      dispatch(getEvents(trip_id))
      dispatch(getTrips())
  }, [dispatch, trip_id])

  
  

  

//This sorts by that distance and assignes start and end times to 'currentevent'
useEffect(() => { 
    const firstEvent = eventsArr[0]

    eventsArr.sort((a, b) => a.order - b.order)

    if(eventsArr.length && tripStartDate) { 
      
      let currentTime = moment(tripStartDate).add(8, 'h').toDate() //Tue Jun 22 2021 00:00:00 GMT-0500 (Central Daylight Time)
      let days = 1;
      for (let i = 0; i < eventsArr.length; i++) { 
        let currentEvent = eventsArr[i]
        if (moment(currentTime).hour() === 8) { 
          currentEvent.start = moment(currentTime).toDate()
        }else {
          currentEvent.start = moment(currentTime).add(currentEvent.distance, 's').toDate()
        }
        currentEvent.end = moment(currentTime).add(currentEvent.duration, 'm').toDate()
        // dispatch(updateEvent(currentEvent.id, currentEvent.order, currentEvent.start,currentEvent.end))
        currentTime = currentEvent.end
        if(moment(currentEvent.end).hour() >= 16) { 
          currentTime = moment(tripStartDate).add(days, 'd').add(8, 'h').toDate()
          days += 1;
        }
      }
    }
  }, [dispatch, eventsArr.length, tripStartDate])

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




  const handleDragEvent = (event) => {
     let oldEvent = event.event
     let newStart = event.start
     let newEnd = event.end
     oldEvent["start"] = newStart
     oldEvent["end"] = newEnd
    // dispatch(updateEvent(oldEvent.id, oldEvent.order, oldEvent.start,oldEvent.end))
  };

  const handleNavigate = (date, view, action) => {
      setDate(date)
  }

  return (startDate && eventsArr.length && 
    <div id="itinerary-page-container">
      <div id="itinerary-title">{(tripEndDate.getTime()-tripStartDate.getTime())/(1000*3600*24)} DAYS IN {chosenTrip[0].name.toUpperCase()}</div>
      <div>
        <DnDCalendar
        localizer={localizer}
        events={eventsArr}
        startAccessor="start"
        endAccessor="end"
        style={{ height: 700 ,
                  width: 1000,
                  margin:50,
              }}
        onEventDrop={handleDragEvent}
        selectable={true}
        resizable={true}
        defaultView="week"
        min={new Date( today.getFullYear(), today.getMonth(), today.getDate(), 8)}
        max={new Date( today.getFullYear(), today.getMonth(), today.getDate(), 19)}
        date={startDate}
        onNavigate={handleNavigate}
        // onSelectSlot={handleSelect}
        // onSelectEvent={handleSelectEvent}
        />
      </div>
    </div>
  );
}

export default Itinerary;





