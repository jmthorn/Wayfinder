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
    print("trips----------------------------------", trips)


    return {"trips": [trip.to_dict() for trip in trips]}


@trips_routes.route('/', methods=['POST'])
@login_required
def add_trip():
    userId = current_user.id
    json_data = request.get_json()
    print(json_data)  #{'chosenCityId': 1, 'startDate': '2021-06-22T05:00:00.000Z', 'endDate': '2021-06-26T05:00:00.000Z'}

    new_trip = Trip(
        user_id= userId,
        city_id=json_data['chosenCityId'],
        start_date=json_data['startDate'],
        end_date=json_data['endDate'],
    )

    db.session.add(new_trip)
    db.session.commit()
    print("NEWTRIP", new_trip)
    return {"trip": new_trip.to_dict()}
