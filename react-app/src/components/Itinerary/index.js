import React, { useState } from 'react';
import { Calendar, momentLocalizer, Views } from 'react-big-calendar'
import { DragDropContext } from "react-dnd";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import moment from 'moment'
import "react-big-calendar/lib/css/react-big-calendar.css"

const Itinerary = () => {

  const localizer = momentLocalizer(moment)
  const DnDCalendar = withDragAndDrop(Calendar);
  const [calendarEvent, setCalendarEvent] = useState({});
  let today = new Date();
  
  
  let dummyEvents = [
      {
          id:1,
          allDay: false,
          end: new Date('May 30, 2021 14:13:00'),
          start: new Date('May 30, 2021 12:13:00'),
          title: 'hi',
        },
        {
            id:2,
            allDay: true,
            end: new Date('December 09, 2017 11:13:00'),
            start: new Date('December 09, 2017 11:13:00'),
            title: 'All Day Event',
        },
    ];
    
    const [events, setEvents] = useState(dummyEvents);

//   const handleSelect = (event, e) => {
//     const { start, end } = event;
//     const data = { title: '', subject: '', start, end, allDay: false };
//     setCalendarEvent(data);
//   };

//   const handleSelectEvent = (event, e) => {

//     let { id, title, subject, start, end, allDay } = event;
//     start = new Date(start);
//     end = new Date(end);
//     const data = { id, title, subject, start, end, allDay };
//     setCalendarEvent(data);
//   };

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
        style={{ height: 500 }}
        onEventDrop={handleDragEvent}
        selectable={true}
        resizable={true}
        defaultView="week"
        // onSelectSlot={handleSelect}
        // onSelectEvent={handleSelectEvent}
        />
  </div>

    </>
  );
}

export default Itinerary;