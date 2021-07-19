from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import City
from app.models import Trip
from app.models import Event
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_
from app.models import db
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from json import loads 
import os




events_routes = Blueprint('events', __name__)


# @events_routes.route('/<trip_id>', methods=['GET'])
# @login_required
# def events(trip_id):
#     userId = current_user.id
#     events = Event.query.filter(Event.trip_id == trip_id).all()
#     return {"events": [event.to_dict() for event in events]}



@events_routes.route('/<trip_id>', methods=['GET'])
@login_required
def events(trip_id):
    userId = current_user.id
    events = Event.query.filter(Event.trip_id == trip_id).all()

    # Sort events based on distance from eachother:

    if len(events) == 0:
        return {"events": []}

    apiKey = os.environ.get('GOOGLE_MAPS_KEY')

    # Grab first event from "events" to set a starting point
    firstEvent = events[0]
    # Query first event from "id" in order to update that event's distance to 0
    event2_to_update = Event.query.get(firstEvent.to_dict()['id'])
    event2_to_update.distance=0

    db.session.add(event2_to_update)
    db.session.commit()

    # Initialize "sortedEvents" with first event 
    sortedEvents = [events[0]]
    #Initialize "newEvents" with the rest of the events
    newEvents = events[1:]
    
    #Loop through each event in sorted events
    for i, val in enumerate(sortedEvents):
        currentNode = sortedEvents[i]
        closestDist=10000000000000
        closestIndex = ''
        #For each node in newEvents, loop through to check each one's distance to "currentNode"
        for j, val in enumerate(newEvents):
            nextNode= newEvents[j]

            # Google Distance Matrix API 
            url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={currentNode.to_dict()["lat"]},{currentNode.to_dict()["lng"]}&destinations={nextNode.to_dict()["lat"]},{nextNode.to_dict()["lng"]}&key={apiKey}'
            reqs = urlopen(Request(url))
            res = loads(reqs.read().decode("UTF-8"))
            # Check status to ensure no errors and assign a driving distance 
            status = res['rows'][0]['elements'][0]['status']
            if status == res['rows'][0]['elements'][0]['status'] == "ZERO_RESULTS":
                duration = 3000
            else:
                duration = res['rows'][0]['elements'][0]['duration']['value']
            # Reassign closesDist to new driving distance if it is closer
            if duration < closestDist:
                closestDist = duration
                closestIndex = j

        if closestDist < 1000000000:

            chosenEvent = newEvents[closestIndex]
            # Update distance to event and save to database
            event_to_update = Event.query.get(chosenEvent.to_dict()['id'])
            event_to_update.distance=closestDist

            db.session.add(event_to_update)
            db.session.commit()

            # Add closest event to sorted Events and remove from newEvents 
            sortedEvents.append(newEvents[closestIndex])
            newEvents = newEvents[:closestIndex] + newEvents[closestIndex+1:]
        #resent the closest distance for the next event
        closestDist=1000000000
        closestIndex = ''

    # Future Implementation: Update and utilize "order" in event

    # for i, val in enumerate(sortedEvents):

    #         chosenEvent3 = sortedEvents[i]
    #         event_to_update = Event.query.get(chosenEvent3.to_dict()['id'])
    #         event_to_update.order=i

    #         db.session.add(event_to_update)
    #         db.session.commit()

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



@events_routes.route('/<event_id>', methods=['PUT'])
@login_required
def update_event(event_id):
    userId = current_user.id
    json_data = request.get_json()
    event_to_update = Event.query.get(json_data['event_id'])

    event_to_update.order=json_data['order']
    event_to_update.start=json_data['start']
    event_to_update.end=json_data['end']

    db.session.add(event_to_update)
    db.session.commit()
    return {"event": event_to_update.to_dict()}

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
