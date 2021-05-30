from app.models import db, Custom_destination

# Adds a demo user, you can add other users here if you want
def seed_custom_destinations():

    D1 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D2 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D3 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D4 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D5 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D6 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D7 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D8 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D9 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D10 = Custom_destination(
        name='', 
        city_id=1,
        description="",
        image_url="",
        address="",
        duration=""
        )

    D11 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D12 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D13 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D14 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D15 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D16 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D17 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D18 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D19 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D20 = Custom_destination(
        name='', 
        city_id=2,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D21 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D22 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D23 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D24 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D25 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D26 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D27 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D28 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D29 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )
    D30 = Custom_destination(
        name='', 
        city_id=3,
        description="",
        image_url="",
        address="",
        duration=""
        )



    db.session.add(D1)
    db.session.add(D2)
    db.session.add(D3)
    db.session.add(D4)
    db.session.add(D5)
    db.session.add(D6)


    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_custom_destinations():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()