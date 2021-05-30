from app.models import db, City

# Adds a demo user, you can add other users here if you want
def seed_cities():

    C1 = City(name='Austin', 
                coutry_id=1)
    C2 = City(name='Los Angeles', 
                coutry_id=1)
    C3 = City(name='Seattle', 
                coutry_id=1)
    C4 = City(name='Bali', 
                coutry_id=3)
    C5 = City(name='Tokyo', 
                coutry_id=2)


    db.session.add(C1)
    db.session.add(C2)
    db.session.add(C3)
    db.session.add(C4)
    db.session.add(C5)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_cities():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
