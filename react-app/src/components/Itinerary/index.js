import React, { useEffect, useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar'
// import { DragDropContext } from "react-dnd";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import moment from 'moment'
import { useDispatch, useSelector } from 'react-redux';
import { getEvents } from '../../store/events';
import { useParams } from 'react-router';
import "react-big-calendar/lib/css/react-big-calendar.css"
import { getTrips } from '../../store/trips';


const Itinerary = () => {

  const events = useSelector(state => state.events)
  const trips = useSelector(state => state?.trips)
  const { trip_id } = useParams()
  const chosenTrip = Object.values(trips).filter((trip) => trip.id === Number(trip_id))
  const eventsArr = Object.values(events)
  const localizer = momentLocalizer(moment)
  // const [calendarEvent, setCalendarEvent] = useState({});
  const DnDCalendar = withDragAndDrop(Calendar);
  const dispatch = useDispatch()
  const today = new Date(); //Mon Jun 07 2021 13:03:45 GMT-0500 (Central Daylight Time) 
  const tripStartDate = new Date(chosenTrip[0]?.start_date) //Tue Jun 22 2021 00:00:00 GMT-0500 (Central Daylight Time)
  const tripEndDate = new Date(chosenTrip[0]?.end_date) 



  useEffect(() => { 
      dispatch(getEvents(trip_id))
      dispatch(getTrips())
  }, [dispatch])


  
  let dummyEvents = [
      {
          id:1,
          // allDay: false,
          end: new Date('May 30, 2021 14:13:00'),
          start: new Date('May 30, 2021 12:13:00'),
          title: 'hi',
        },
        {
            id:2,
            // allDay: true,
            end: new Date('December 09, 2017 11:13:00'),
            start: new Date('December 09, 2017 11:13:00'),
            title: 'All Day Event',
        },
    ];
    
    // const [events, setEvents] = useState(dummyEvents);


  const handleDragEvent = (event) => {
    //  console.log(event) {start: Sun May 30 2021 10:00:00 GMT-0500 (Central Daylight Time), end: Sun May 30 2021 12:00:00 GMT-0500 (Central Daylight Time), resourceId: null, event: {…}}
    //  console.log(event.event) {id: 1, allDay: false, end: Sun May 30 2021 14:13:00 GMT-0500 (Central Daylight Time), start: Sun May 30 2021 12:13:00 GMT-0500 (Central Daylight Time), title: "hi"}
     let oldEvent = event.event
     let newStart = event.start
     let newEnd = event.end
     oldEvent["start"] = newStart
     oldEvent["end"] = newEnd
  };


  return (
    <>
        <div>
        <DnDCalendar
        localizer={localizer}
        events={dummyEvents}
        startAccessor="start"
        endAccessor="end"
        style={{ height: 700 ,
                  width: 1000,
                  margin: 50,
              }}
        onEventDrop={handleDragEvent}
        selectable={true}
        resizable={true}
        defaultView="week"
        min={new Date( today.getFullYear(), today.getMonth(), today.getDate(), 8)}
        max={new Date( today.getFullYear(), today.getMonth(), today.getDate(), 17)}
        date={tripStartDate}
        // onSelectSlot={handleSelect}
        // onSelectEvent={handleSelectEvent}
        />
  </div>

    </>
  );
}

export default Itinerary;