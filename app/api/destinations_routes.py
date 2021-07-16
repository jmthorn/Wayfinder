from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.forms import UpdateDestinationsForm, CreateDestinationsForm
from app.models import City
from app.models import Default_destination
from app.models import Custom_destination
from sqlalchemy import and_
from app.models import db
from app.aws import upload_file_to_s3, allowed_file, get_unique_filename

destinations_routes = Blueprint('destinations', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages

    

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
    print("REQUESTTTTTTTTTTTT", request.files.getlist)
    image = request.files["image_url"]
    print("IMAGEEEEE BACKENDDDD", image.filename)

    # upload image to S3

    if not allowed_file(image.filename): 
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)
    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]
    # create new destination

    new_destination = Custom_destination(
        user_id= userId,
        city_id=request.form["cityId"],
        image_url=url,
        address=request.form["address"],
        name=request.form["name"],
        lat=request.form["lat"],
        lng=request.form["lng"],
        duration=request.form["duration"],
        description=request.form["description"],
    )

    db.session.add(new_destination)
    db.session.commit()
    userId = current_user.id
    default_destinations = Default_destination.query.filter(Default_destination.city_id == request.form["cityId"]).all()
    custom_destinations = Custom_destination.query.filter(and_(Custom_destination.city_id == request.form["cityId"], Custom_destination.user_id == userId)).all()

    return {"default_destinations": [destination.to_dict() for destination in default_destinations], "custom_destinations": [destination.to_dict() for destination in custom_destinations]}

#update destination
@destinations_routes.route('/<destinationId>', methods=['PUT'])
@login_required
def update_destination(destinationId):  
    userId = current_user.id
    json_data = request.get_json()
    # print(json_data)
    {'name': "Sir John Soane's Museum, 13 Lincoln's Inn Fields, London WC2A 3BP, United Kingdom", 'description': "Sir John Soane's Museums", 'image_url': "This is, without a doubt, the city’s most atmospheric museum, packed to the rafters with hundreds of interesting and impressive artworks and artifact ... (199 characters truncated) ... he unobservant might miss. It's not the unknown it once was though, so unless you go first thing in the morning you'll probably have to wait in line.", 'address': "https://media.cntraveler.com/photos/5a7b4d29b7a3db05bf40e1d4/1:1/w_1024%2Cc_limit/Sir-John-Soane's__2018_The-Picture-Room---Photo-Gareth-Gardner.jpg", 'lat': 60, 'lng': 51.51703819999999, 'duration': -0.1174699, 'custom_destinations_id': 9}

    destination_to_update = Custom_destination.query.get(json_data['destinationId'])

    destination_to_update.city_id=json_data['city_id']
    destination_to_update.image_url=json_data['image_url']
    destination_to_update.address=json_data['address']
    destination_to_update.name=json_data['name']
    destination_to_update.lat=json_data['lat']
    destination_to_update.lng=json_data['lng']
    destination_to_update.duration=json_data['duration']
    destination_to_update.description=json_data['description']

    db.session.add(destination_to_update)
    db.session.commit()

    default_destinations = Default_destination.query.filter(Default_destination.city_id == json_data['city_id']).all()
    custom_destinations = Custom_destination.query.filter(and_(Custom_destination.city_id == json_data['city_id'], Custom_destination.user_id == userId)).all()

    return {"destination": destination_to_update.to_dict(), "default_destinations": [destination.to_dict() for destination in default_destinations], "custom_destinations": [destination.to_dict() for destination in custom_destinations]}



#delete destination
@destinations_routes.route('/<destinationId>', methods=['DELETE'])
@login_required
def delete_destination(destinationId):
    userId = current_user.id
    json_data = request.get_json()
    destination_to_delete = Custom_destination.query.get(json_data['destinationId'])

    db.session.delete(destination_to_delete)
    db.session.commit()
    userId = current_user.id
    default_destinations = Default_destination.query.filter(Default_destination.city_id == destination_to_delete.city_id).all()
    custom_destinations = Custom_destination.query.filter(and_(Custom_destination.city_id == destination_to_delete.city_id, Custom_destination.user_id == userId)).all()

    return {"default_destinations": [destination.to_dict() for destination in default_destinations], "custom_destinations": [destination.to_dict() for destination in custom_destinations]}
