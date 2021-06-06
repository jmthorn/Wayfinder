import os
from flask import Blueprint


api_routes = Blueprint('api', __name__)


@api_routes.route('/')
def get_api_key():
  return {"apiKey": os.environ.get('GOOGLE_MAPS_KEY')}