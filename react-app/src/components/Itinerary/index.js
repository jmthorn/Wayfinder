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
  const trips = useSelector(state => state.trips)
  const { trip_id } = useParams()
  const chosenTrip = Object.values(trips).filter((trip) => trip.id === Number(trip_id))
  const eventsArr = Object.values(events)
  const localizer = momentLocalizer(moment)
  // const [calendarEvent, setCalendarEvent] = useState({});
  const DnDCalendar = withDragAndDrop(Calendar);
  const dispatch = useDispatch()
  const today = new Date(); //Mon Jun 07 2021 13:03:45 GMT-0500 (Central Daylight Time) 
  const tripStartDate = new Date(chosenTrip[0]?.start_date) //Tue Jun 22 2021 00:00:00 GMT-0500 (Central Daylight Time)
  // const tripEndDate = new Date(chosenTrip[0]?.end_date) 
  const [startDate, setDate] = useState("")


  useEffect(() => { 
    if (chosenTrip.length) { 
      setDate(new Date(chosenTrip[0].start_date))
    }
  }, [chosenTrip.length])

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

  const handleNavigate = (date, view, action) => {
      console.log(typeof date, view, action)
      setDate(date)
  }

  return startDate && (
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
        date={startDate}
        onNavigate={handleNavigate}
        // onSelectSlot={handleSelect}
        // onSelectEvent={handleSelectEvent}
        />
  </div>

    </>
  );
}

export default Itinerary;





// function haversineDiff (locationObject1, locationObject2) {
//   const radiusOfTheEarthInDesiredUnits = 3958.8;
//   const latitudeDifferentialInRadians = rad(locationObject2.latitude - locationObject1.latitude);
//   const longitudeDifferentialInRadians = rad(locationObject2.longitude - locationObject1.longitude);
//   const noIdea =
//     Math.sin(latitudeDifferentialInRadians / 2) * Math.sin(latitudeDifferentialInRadians / 2) +
//     Math.cos(rad(locationObject1.latitude)) * Math.cos(rad(locationObject2.latitude)) *
//     Math.sin(longitudeDifferentialInRadians / 2) * Math.sin(longitudeDifferentialInRadians / 2)
//     ;
//   const noIdea2 = 2 * Math.atan2(Math.sqrt(noIdea), Math.sqrt(1 - noIdea));
//   return radiusOfTheEarthInDesiredUnits * noIdea2;
// }


// itinerary.sort((a, b) => a - b)