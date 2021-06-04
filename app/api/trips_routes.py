from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import City
from app.models import Trip
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_
from app.models import db




trips_routes = Blueprint('trips', __name__)


@trips_routes.route('/', methods=['GET'])
@login_required
def trips():
    userId = current_user.id
    trips = Trip.query.filter(Trip.user_id == userId).all()


    return {"trips": [trip.to_dict() for trip in trips]}


@trips_routes.route('/', methods=['POST'])
@login_required
def add_trip():
    userId = current_user.id
    json_data = request.get_json()
    # print(json_data)  #{'chosenCityId': 1, 'startDate': '2021-06-22T05:00:00.000Z', 'endDate': '2021-06-26T05:00:00.000Z'}

    new_trip = Trip(
        user_id= userId,
        city_id=json_data['chosenCityId'],
        start_date=json_data['startDate'],
        end_date=json_data['endDate'],
    )

    db.session.add(new_trip)
    db.session.commit()
    return {"trip": new_trip.to_dict()}

@trips_routes.route('/<tripId>', methods=['PUT'])
@login_required
def update_trip(tripId):
    userId = current_user.id
    json_data = request.get_json()
    # print(json_data) {'chosenTripId': 1, 'startDate': '2021-06-01T05:00:00.000Z', 'endDate': '2021-06-05T05:00:00.000Z'}
    trip_to_update = Trip.query.get(json_data['chosenTripId'])

    trip_to_update.start_date=json_data['startDate']
    trip_to_update.end_date=json_data['endDate']

    db.session.add(trip_to_update)
    db.session.commit()
    return {"trip": trip_to_update.to_dict()}

@trips_routes.route('/<chosenTripId>', methods=['DELETE'])
@login_required
def delete_trip(chosenTripId):
    userId = current_user.id
    json_data = request.get_json()

    trip_to_delete = Trip.query.get(json_data['chosenTripId'])

    db.session.delete(trip_to_delete)
    db.session.commit()
    return {"trip": trip_to_delete.to_dict_wo_cities()}
