import React, { useEffect, useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar'
// import { DragDropContext } from "react-dnd";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import moment from 'moment'
import { useDispatch, useSelector } from 'react-redux';
import { getEvents } from '../../store/events';
import { useParams } from 'react-router';
import "react-big-calendar/lib/css/react-big-calendar.css"


const Itinerary = () => {

  const events = useSelector(state => state.events)
  const eventsArr = Object.values(events)
  const localizer = momentLocalizer(moment)
  const DnDCalendar = withDragAndDrop(Calendar);
  const dispatch = useDispatch()
  const { trip_id } = useParams()
  const today = new Date();

  // const [calendarEvent, setCalendarEvent] = useState({});
  // let today = new Date();

  useEffect(() => { 
      dispatch(getEvents(trip_id))
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
        // onSelectSlot={handleSelect}
        // onSelectEvent={handleSelectEvent}
        />
  </div>

    </>
  );
}

export default Itinerary;