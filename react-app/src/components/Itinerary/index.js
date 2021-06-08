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
import distance from 'google-distance-matrix';
// var distance = require('google-distance-matrix');



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
  // const tripEndDate = new Date(chosenTrip[0]?.end_date) 
  const [startDate, setDate] = useState("")
  const [apiKey, setApiKey] = useState('');

  useEffect(() => {
  (async()=> {
    const res = await fetch('/api/retrieve_api/');
    const { apiKey } = await res.json();
    setApiKey(apiKey);

    })()
  })


  useEffect(() => { 
    if (chosenTrip.length) { 
      setDate(new Date(chosenTrip[0].start_date))
    }
  }, [chosenTrip.length])

  useEffect(() => { 
      dispatch(getEvents(trip_id))
      dispatch(getTrips())
  }, [dispatch])

  
  

  
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//Use the Google Maps Distance Matrix API to sort and assign drive times. 


  // useEffect(() => (async()=> {

  //   if(apiKey) { 
    //   let sortedArr = [eventsArr[0]]
    //   let newArr = eventsArr.slice(1)
    //   for (let i = 0; i < sortedArr.length; i++) { 
    //     let currentSortedEvent = sortedArr[i]
    //     let closestDistance = Infinity
    //     let closestIndex = null;
    //     for (let j = 0 ; j < newArr.length; j++) { 
    //       let currentUnsortedEvent = eventsArr[i]
    //       let distanceBetweenBoth;
    //       //TODO REQUEST DISTANCE

    //       const res = await fetch('https://maps.googleapis.com/maps/api/distancematrix/json?origins=heading=90:37.773279,-122.468780&destinations=37.773245,-122.469502&key=AIzaSyB5ifGzUeagcjHV-bjuPJO75jQGwCzfpno');
    //       const data = res.json()
          
  
    //     }
    //     sortedArr.push(closestIndex)
    //     // closestDistance = Infinity
    //     closestIndex = null;
    //   }
    // }

  // }), [, apiKey, eventsArr.length])



// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  
  //   const rad = function(x) {
  //     return x * Math.PI / 180;
  //   };
  
  //   // Haversine Formula was provided by TA JM 
  //   function haversineDiff (locationObject1, locationObject2) {
  //   const radiusOfTheEarthInDesiredUnits = 3958.8;
  //   const latitudeDifferentialInRadians = rad(locationObject2.lat - locationObject1.lat);
  //   const longitudeDifferentialInRadians = rad(locationObject2.lng - locationObject1.lng);
  //   const noIdea =
  //     Math.sin(latitudeDifferentialInRadians / 2) * Math.sin(latitudeDifferentialInRadians / 2) +
  //     Math.cos(rad(locationObject1.lat)) * Math.cos(rad(locationObject2.lat)) *
  //     Math.sin(longitudeDifferentialInRadians / 2) * Math.sin(longitudeDifferentialInRadians / 2)
  //     ;
  //   const noIdea2 = 2 * Math.atan2(Math.sqrt(noIdea), Math.sqrt(1 - noIdea));
  //   return radiusOfTheEarthInDesiredUnits * noIdea2;
  // }

//This uses the haversine formula to find distance, then sorts by that distance and assignes start and end times to 'currentevent'
// useEffect(() => { 
//     const firstEvent = eventsArr[0]

//     if(eventsArr.length && startDate) { 
//       for (let i = 0; i<eventsArr.length;i++) { 
//         let currentEvent = eventsArr[i]
//         let distance = haversineDiff(currentEvent, firstEvent)
//         currentEvent['distance'] = distance
//       }

//       eventsArr.sort((a, b) => a.distance - b.distance)
//       console.log("2",eventsArr)
//       let currentTime = moment(startDate).add(8, 'h').toDate() //Tue Jun 22 2021 00:00:00 GMT-0500 (Central Daylight Time)
//       let days = 0;
//       for (let i = 0; i < eventsArr.length; i++) { 
//         let currentEvent = eventsArr[i]
//         currentEvent.start = currentTime
//         currentEvent.end = moment(currentTime).add(currentEvent.duration, 'm').toDate()
//         currentTime = currentEvent.end
//         console.log(currentEvent)
//         if(moment(currentEvent.end).hour() > 16) { 
//           currentTime = moment(startDate).add(1, 'd').add(8, 'h').toDate()
//           days += 1;
//         }
//       }
//     }
//   }, [dispatch, eventsArr.length, startDate])

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








  const handleDragEvent = (event) => {
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
        events={eventsArr}
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
        max={new Date( today.getFullYear(), today.getMonth(), today.getDate(), 18)}
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







// itinerary.sort((a, b) => a - b)




  // let dummyEvents = [
  //     {
  //         id:1,
  //         // allDay: false,
  //         end: new Date('May 30, 2021 14:13:00'),
  //         start: new Date('May 30, 2021 12:13:00'),
  //         title: 'hi',
  //       },
  //       {
  //           id:2,
  //           // allDay: true,
  //           end: new Date('December 09, 2017 11:13:00'),
  //           start: new Date('December 09, 2017 11:13:00'),
  //           title: 'All Day Event',
  //       },
  //   ];