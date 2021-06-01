from app.models import db, Custom_destination

# Adds a demo user, you can add other users here if you want
def seed_custom_destinations():

    D1 = Custom_destination(
        name='Torchy\'s Tacos', 
        city_id=1,
        description="An Austin original serving specialty tacos made with a passion. Torchy’s customers, employees, friends and fans share in the Taco Dream. Prepare to be addicted! Several Austin area locations.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d1.jpeg",
        address="1822 S Congress Ave, Austin, TX 78704",
        lat=30.245621744100376,
        lng= -97.75158020244523,
        duration=60,
        user_id=1
        )
    D2 = Custom_destination(
        name='Slurpin\' Ramen Bar', 
        city_id=2,
        description="Started in the heart of Koreatown, Los Angeles 8th Street, Slurpin ramen was created from ambition to bringing authentic Hakata-style  rich, thick and creamy tonkotsu ramen to California. Slurpin’ derives from Japanese culture in showing respect to your ramen chef with a loud “slurp” sound from eating the noodles and broth.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d2.jpeg",
        address="3500 W 8th St, Los Angeles, CA 90005",
        lat=34.07001707893153,
        lng= -118.30809265784463,
        duration=60,
        user_id=1
        )
    D3 = Custom_destination(
        name='Gas Works Park', 
        city_id=3,
        description="Gas Works Park is a park located in Seattle, Washington, United States. It is a 19.1-acre public park on the site of the former Seattle Gas Light Company gasification plant, located on the north shore of Lake Union at the south end of the Wallingford neighborhood.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d3.jpg",
        address="2101 N Northlake Way, Seattle, WA 98103",
        lat=47.64630557402461,
        lng= -122.33368897320506,
        duration=120,
        user_id=1
        )
    D4 = Custom_destination(
        name='Toufuya Ukai', 
        city_id=5,
        description="The restaurant features beautiful pine trees and a pond where Koi carp swim. Passing in front of the garden lantern and waterwheel and walking on the steppingstones, you will find yourself back in time in the town of Edo, the Tokyo of 200 years ago. Please enjoy the extraordinary atmosphere in the restaurant with 6,600 m² of extensive Japanese gardens located at the foot of Tokyo Tower.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d4.jpeg",
        address="4 Chome-4-13 Shibakoen, Minato City, Tokyo 105-0011, Japan",
        lat=37.70220703131334,
        lng= 139.89131454959846,
        duration=80,
        user_id=1
        )
    D5 = Custom_destination(
        name='Ling-Ling\'s Bali', 
        city_id=4,
        description="Located in the heart of Seminyak, Ling Ling's offers contemporary asian fusion basing our core ideals on Japanese & Korean styles. We strive for our customers satisfaction with our endless supply of asian tapas to our most delectable drinks menu. Open from 12pm everyday to satisfy your hunger for an exquisite meal, a heavenly refreshment, tunes for the soul or just a fun night out with friends.",
        image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/d5.jpeg",
        address="Jl. Petitenget no. 43B, Seminyak 80361 Indonesia",
        lat=-8.673867098817842,
        lng= 115.15738463949066,
        duration=80,
        user_id=1
        )
    # D4 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D5 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D6 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D7 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D8 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D9 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D10 = Custom_destination(
    #     name='', 
    #     city_id=1,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )

    # D11 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D12 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D13 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D14 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D15 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D16 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D17 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D18 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D19 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D20 = Custom_destination(
    #     name='', 
    #     city_id=2,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D21 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D22 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D23 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D24 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D25 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D26 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D27 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D28 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D29 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )
    # D30 = Custom_destination(
    #     name='', 
    #     city_id=3,
    #     description="",
    #     image_url="",
    #     address="",
    #     duration=""
    #     )



    db.session.add(D1)
    db.session.add(D2)
    db.session.add(D3)
    db.session.add(D4)
    db.session.add(D5)



    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_custom_destinations():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()