from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import City
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_


destinations_routes = Blueprint('destinations', __name__)

#get all destinations per city
@destinations_routes.route('/<cityId>')
@login_required
def destinations(cityId):
    userId = current_user.id
    default_destinations = Default_destination.query.filter(Default_destination.city_id == cityId).all()
    custom_destinations = Custom_destination.query.filter(and_(Custom_destination.city_id == cityId, Custom_destination.user_id == userId)).all()

    return {"default_destinations": [destination.to_dict() for destination in default_destinations], "custom_destinations": [destination.to_dict() for destination in custom_destinations]}


# get destination
@destinations_routes.route('/destination/<destinationName>')
@login_required
def destination(destinationName):

    dest_list = destinationName.split("_")
    string=" "
    dest_name = string.join(dest_list)
    c_destination= Custom_destination.query.filter(Custom_destination.name == str(dest_name)).first()
    d_destination= Default_destination.query.filter(Default_destination.name == str(dest_name)).first()

    if(d_destination):
        return {"destination": d_destination.to_dict()}
    if(c_destination):
        return {"destination": c_destination.to_dict()}


# create destination
@destinations_routes.route('/', methods=['POST'])
@login_required
def add_destination():
    userId = current_user.id
    json_data = request.get_json()

    new_destination = Custom_destination(
        user_id= userId,
        city_id=json_data['cityId'],
        image_url=json_data['image_url'],
        address=json_data['address'],
        name=json_data['name'],
        lat=json_data['lat'],
        lng=json_data['lng'],
        duration=json_data['duration'],
        description=json_data['description'],
    )

    db.session.add(new_destination)
    db.session.commit()
    return {"destination": new_destination.to_dict()}

#update destination
@destinations_routes.route('/<destinationId>', methods=['PUT'])
@login_required
def update_destination(destinationId):
    userId = current_user.id
    json_data = request.get_json()
    # print(json_data) {'chosenTripId': 1, 'startDate': '2021-06-01T05:00:00.000Z', 'endDate': '2021-06-05T05:00:00.000Z'}
    destination_to_update = Custom_destination.query.get(json_data['destinationId'])

    destination_to_update.city_id=json_data['cityId']
    destination_to_update.image_url=json_data['image_url']
    destination_to_update.address=json_data['address']
    destination_to_update.name=json_data['name']
    destination_to_update.lat=json_data['lat']
    destination_to_update.lng=json_data['lng']
    destination_to_update.duration=json_data['duration']
    destination_to_update.description=json_data['description']

    db.session.add(destination_to_update)
    db.session.commit()
    return {"destination": destination_to_update.to_dict()}

#delete destination
@destinations_routes.route('/<destinationId>', methods=['DELETE'])
@login_required
def delete_destination(destinationId):
    userId = current_user.id
    json_data = request.get_json()

    destination_to_delete = Custom_destination.query.get(json_data['destinationId'])

    db.session.delete(destination_to_delete)
    db.session.commit()
    return {"destination": destination_to_delete.to_dict()}
