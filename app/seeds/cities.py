from app.models import db, City

# Adds a demo user, you can add other users here if you want
def seed_cities():

    C1 = City(name='Austin', 
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/Austin.jpeg",
                coutry_id=1)
    C2 = City(name='Los Angeles', 
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/LA.jpeg", 
                coutry_id=1)
    C3 = City(name='Seattle',
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/Seattle.jpeg", 
                coutry_id=1)
    C4 = City(name='Bali', 
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/Bali.jpeg", 
                coutry_id=3)
    C5 = City(name='Tokyo', 
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/Tokyo.jpeg", 
                coutry_id=2)
    C6 = City(name='London', 
                image_url="https://wayfinder-images.s3.us-east-2.amazonaws.com/London.jpeg", 
                coutry_id=4)


    db.session.add(C1)
    db.session.add(C2)
    db.session.add(C3)
    db.session.add(C4)
    db.session.add(C5)
    db.session.add(C6)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_cities():
    db.session.execute('TRUNCATE cities RESTART IDENTITY CASCADE;')
    db.session.commit()
