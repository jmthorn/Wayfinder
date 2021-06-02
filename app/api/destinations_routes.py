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

