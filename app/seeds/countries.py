from app.models import db, Country

# Adds a demo user, you can add other users here if you want
def seed_countries():

    C1 = Country(name='United States')
    C2 = Country(name='Japan')
    C3 = Country(name='Indonesia')
    C4 = Country(name='United Kingdom')

    db.session.add(C1)
    db.session.add(C2)
    db.session.add(C3)
    db.session.add(C4)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_countries():
    db.session.execute('TRUNCATE countries RESTART IDENTITY CASCADE;')
    db.session.commit()
