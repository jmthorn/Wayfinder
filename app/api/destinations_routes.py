from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import City
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_


destinations_routes = Blueprint('destinations', __name__)


@destinations_routes.route('/<cityId>')
@login_required
def destinations(cityId):
    userId = current_user.id
    default_destinations = Default_destination.query.filter(Default_destination.city_id == cityId).all()
    custom_destinations = Custom_destination.query.filter(and_(Custom_destination.city_id == cityId, Custom_destination.user_id == userId)).all()

    return {"default_destinations": [destination.to_dict() for destination in default_destinations], "custom_destinations": [destination.to_dict() for destination in custom_destinations]}



@destinations_routes.route('/destination/<destinationName>')
@login_required
def destination(destinationName):
    txt = "welcome-to-the-jungle"

    dest_list = destinationName.split("_")
    string=" "
    dest_name = string.join(dest_list)
    c_destination= Custom_destination.query.filter(Custom_destination.name == str(dest_name)).first()
    d_destination= Default_destination.query.filter(Default_destination.name == str(dest_name)).first()

    if(d_destination):
        return {"destination": d_destination.to_dict()}
    if(c_destination):
        return {"destination": c_destination.to_dict()}
