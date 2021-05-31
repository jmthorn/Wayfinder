from app.models import db, Trip
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_trips():

    start_date = "6/10/2021 8:00:00"
    end_date = "6/12/2021 16:00:00"

    date_format = "%d/%m/%Y %H:%M:%S"

    # create datetime objects from the strings
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    # now = datetime.now()

    T1 = Trip(user_id=1, 
        city_id=1,
        start_date=start,
        end_date=end
        )



    db.session.add(T1)


    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_trips():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
