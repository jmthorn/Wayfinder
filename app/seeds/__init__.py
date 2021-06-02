from flask.cli import AppGroup
from .users import seed_users, undo_users
from .countries import seed_countries, undo_countries
from .cities import seed_cities, undo_cities
from .trips import seed_trips, undo_trips
from .events import seed_events, undo_events
from .default_destinations import seed_default_destinations, undo_default_destinations
from .custom_destinations import seed_custom_destinations, undo_custom_destinations
from .events import seed_events, undo_events

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_countries()
    seed_cities()
    seed_trips()
    seed_custom_destinations()
    seed_default_destinations()
    seed_events()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_countries()
    undo_cities()
    undo_trips()
    undo_custom_destinations()
    undo_default_destinations()
    undo_events()
    # Add other undo functions here
