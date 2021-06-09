# Welcome to ArchiBnb

In this itinerary builder, a user can look up destinations by city and add them to their trip. After adding destinations, an itinerary will be produced, displaying an optimized time schedule of events.

A live Link to the website can be found here: https://wayfinder-app.herokuapp.com/

## A walkthrough of the website

![](https://wayfinder-images.s3.us-east-2.amazonaws.com/gif1.gif)

<!-- ![](https://archibnb-images.s3.us-east-2.amazonaws.com/2-20.gif) -->

<!-- ![](https://archibnb-images.s3.us-east-2.amazonaws.com/3-20.gif) -->

### Technologies

#### Front End

- JavaScript
- HTML
- CSS
- React
- Redux
- Hosted on Heroku

#### Back End

- PostgreSQL
- Express.js
- SQLAlchemy
- Flask

## Functionalities

- User authentication is completed by hashing passwords using bcrypt js library (csurf protected as well)
- The user can search for properties around the world by entering the location, booking dates and guest count.
- Once logged in, a user can navigate through "Places" and book a trip with start and end dates.
- The user can then navigate to destinations within that "Place" to add to their booked trip.
- A logged in user can add custom destinations if their desired destination is not available.
- Onced booked, the user can update or cancel their trip in "MyTrips".
- On the "MyTrips" page, the user can also navigate to the itinerary for each trip, which will display an optimized trip schedule.

## Challenges

- One of the more challanging parts of this application was producing the optimized itinerary. Once the user adds an event to their trip or creates a custom event using the address of the destination, a latitude and longitude coordinate for the location entered is produced using the Google Geocode API. Using those coordinates, the itinerary can be produced by sorting each event by proximity to one another using driving duration in seconds, found using the Google Distance Matrix API. The events are then assigned a start and end time within the trip start and end dates and only between waking hours. When an event is deleted from the trip, the itinerary is dynamically updated to account for its deletion.

## Backend itinerary routes code snippets:

```

events_routes = Blueprint('events', __name__)

@events_routes.route('/<trip_id>', methods=['GET'])
@login_required
def events(trip_id):
    userId = current_user.id
    events = Event.query.filter(Event.trip_id == trip_id).all()

    # print('+++++++++++++++++++++++++++++++++++++++++++++')
    # Sort events based on distance from eachother:

    apiKey = os.environ.get('GOOGLE_MAPS_KEY')
    firstEvent = events[0]
    event2_to_update = Event.query.get(firstEvent.to_dict()['id'])
    event2_to_update.distance=0

    db.session.add(event2_to_update)
    db.session.commit()
    sortedEvents = [events[0]]
    newEvents = events[1:]

    for i, val in enumerate(sortedEvents):
        currentNode = sortedEvents[i]
        closestDist=10000000000000
        closestIndex = ''
        for j, val in enumerate(newEvents):
            nextNode= newEvents[j]
            url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={currentNode.to_dict()["lat"]},{currentNode.to_dict()["lng"]}&destinations={nextNode.to_dict()["lat"]},{nextNode.to_dict()["lng"]}&key={apiKey}'
            reqs = urlopen(Request(url))
            res = loads(reqs.read().decode("UTF-8"))
            duration = res['rows'][0]['elements'][0]['duration']['value']
            if duration < closestDist:
                closestDist = duration
                closestIndex = j

        if closestDist < 1000000000:

            chosenEvent = newEvents[closestIndex]

            event_to_update = Event.query.get(chosenEvent.to_dict()['id'])
            event_to_update.distance=closestDist

            db.session.add(event_to_update)
            db.session.commit()

            sortedEvents.append(newEvents[closestIndex])
            newEvents = newEvents[:closestIndex] + newEvents[closestIndex+1:]

        closestDist=1000000000
        closestIndex = ''

    for i, val in enumerate(sortedEvents):

            chosenEvent3 = sortedEvents[i]
            event_to_update = Event.query.get(chosenEvent3.to_dict()['id'])
            event_to_update.order=i

            db.session.add(event_to_update)
            db.session.commit()

    return {"events": [event.to_dict() for event in sortedEvents]}



@events_routes.route('/', methods=['POST'])
@login_required
def add_event():
    userId = current_user.id
    json_data = request.get_json()
    if 'custom_destination_id' in json_data.keys():
        new_event = Event(
            trip_id= json_data['trip_id'],
            custom_destination_id=json_data['custom_destination_id'],
        )
    else:
        new_event = Event(
            trip_id= json_data['trip_id'],
            default_destination_id=json_data['default_destination_id'],
        )

    db.session.add(new_event)
    db.session.commit()
    return {"event": new_event.to_dict()}



@events_routes.route('/<event_id>', methods=['DELETE'])
@login_required
def event(event_id):
    userId = current_user.id
    json_data = request.get_json()

    event_to_delete = Event.query.get(event_id)
    db.session.delete(event_to_delete)
    # db.session.expire_on_commit = False
    db.session.commit()
    # {'id': 9, 'trip_id': 17, 'order': None, 'default_destination_id': None, 'custom_destination_id': 27, 'start': None, 'end': None, 'name': "Sir John Soane's Museum", 'duration': 60}
    return {"event": event_to_delete.to_dict_wo_ll()}


```

## Frontend itinerary routes code snippets:

```

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
        currentTime = currentEvent.end
        if(moment(currentEvent.end).hour() >= 16) {
          currentTime = moment(tripStartDate).add(days, 'd').add(8, 'h').toDate()
          days += 1;
        }
      }
    }
  }, [dispatch, eventsArr.length, tripStartDate])


  const handleDragEvent = (event) => {
     let oldEvent = event.event
     let newStart = event.start
     let newEnd = event.end
     oldEvent["start"] = newStart
     oldEvent["end"] = newEnd
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
        />
      </div>
    </div>
  );
}

export default Itinerary;

```

## The Wayfinder Creator

- [@jmthorn](https://github.com/jmthorn) 🐈
