from app.models import db, Event

# Adds a demo user, you can add other users here if you want
def seed_events():

    E1 = Event(trip_id='1',
        default_destination_id=1,
        )
    E2 = Event(trip_id='1',
        default_destination_id=2,
        )
    E3 = Event(trip_id='1',
        default_destination_id=3,
        )
    E4 = Event(trip_id='1',
        default_destination_id=4,
        )
    E5 = Event(trip_id='1',
        default_destination_id=5,
        )

    db.session.add(E1)
    db.session.add(E2)
    db.session.add(E3)
    db.session.add(E4)
    db.session.add(E5)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_events():
    db.session.execute('TRUNCATE events RESTART IDENTITY CASCADE;')
    db.session.commit()
