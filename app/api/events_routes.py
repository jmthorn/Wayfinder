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


@events_routes.route('/<trip_id>', methods=['GET'])
@login_required
def events(trip_id):
    userId = current_user.id
    events = Event.query.filter(Event.trip_id == trip_id).all()
    return {"events": [event.to_dict() for event in events]}


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
