from app.models import db, Custom_destination

# Adds a demo user, you can add other users here if you want
def seed_custom_destinations():

    D1 = Custom_destination(
        name='Torchy\'s Tacos', 
        city_id=1,
        description="An Austin original serving specialty tacos made with a passion. Torchy’s customers, employees, friends and fans share in the Taco Dream. Prepare to be addicted! Several Austin area locations.",
        image_url="https://cdn.vox-cdn.com/thumbor/C2lydIPDJ9e3iECfXMZkZSae3N4=/0x0:842x842/1200x800/filters:focal(354x354:488x488)/cdn.vox-cdn.com/uploads/chorus_image/image/58261045/Screen_Shot_2017_08_31_at_2.54.14_PM.0.png",
        address="1822 S Congress Ave, Austin, TX 78704",
        lat=30.245621744100376,
        long= -97.75158020244523,
        duration="60",
        user_id=1
        )
    D2 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration="",
        user_id=1
        )
    D3 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration="",
        user_id=1
        )
    D3 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration="",
        user_id=1
        )
    D3 = Custom_destination(
        name='', 
        city_id=4,
        description="",
        image_url="",
        address="",
        duration="",
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



    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_custom_destinations():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()