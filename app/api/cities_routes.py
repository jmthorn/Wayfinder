from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import City

cities_routes = Blueprint('cities', __name__)


@cities_routes.route('/')
@login_required
def cities():
    print("HELLLOOO FROM BACKEND!!")
    user_id = current_user.id
    cities = City.query.all()
    return {"cities": [city.to_dict() for city in cities]}

