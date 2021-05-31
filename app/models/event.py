from .db import db


class Event(db.Model):
  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key = True)
  trip_id = db.Column(db.Integer, nullable = False)
  order = db.Column(db.Integer, nullable = True)
  default_destination_id = db.Column(db.Integer, nullable=True)
  custom_destination_id = db.Column(db.Integer, nullable=True)
  start = db.Column(db.Datetime, nullable=True)
  end = db.Column(db.Datetime, nullable=True)



  def to_dict(self):
    return {
      "id": self.id,
      "trip_id": self.trip_id,
      "order":self.order,
      "default_destination_id": self.default_destination_id,
      "custom_destination_id": self.custom_destination_id,
      "start": self.start,
      "end": self.end,
      "title": self.title

    }
