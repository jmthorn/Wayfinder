from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import City
from app.models import Trip
from app.models import Event
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_
from app.models import db




events_routes = Blueprint('events', __name__)


@events_routes.route('/', methods=['GET'])
@login_required
def events():
    userId = current_user.id
    json_data = request.get_json()

    events = Event.query.filter(Event.trip_id == json_data['tripId']).all()


    return {"events": [event.to_dict() for event in events]}


@events_routes.route('/', methods=['POST'])
@login_required
def add_event():
    userId = current_user.id
    json_data = request.get_json()

    new_event = Event(
        trip_id= json_data['tripId'],
        order = null,
        default_destination_id=json_data['default_destination_id'],
        custom_destination_id=json_data['custom_destination_id'],
        start=json_data['startDate'],
        end=json_data['endDate'],
    )

    db.session.add(new_event)
    db.session.commit()
    return {"event": new_event.to_dict()}

@events_routes.route('/<eventId>', methods=['PUT'])
@login_required
def update_event(eventId):
    userId = current_user.id
    json_data = request.get_json()
    event_to_update = Event.query.get(json_data['chosenEventId'])

    event_to_update.order=json_data['order']
    event_to_update.start=json_data['startDate']
    event_to_update.end=json_data['endDate']

    db.session.add(event_to_update)
    db.session.commit()
    return {"event": event_to_update.to_dict()}

@events_routes.route('/<chosenEventId>', methods=['DELETE'])
@login_required
def delete_trip(chosenEventId):
    userId = current_user.id
    json_data = request.get_json()

    event_to_delete = Event.query.get(json_data['chosenEventId'])

    db.session.delete(event_to_delete)
    db.session.commit()
    return {"event": event_to_delete.to_dict()}
