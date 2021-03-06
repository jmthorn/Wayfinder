from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Event(db.Model):
  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key = True)
  trip_id = db.Column(db.Integer,ForeignKey("trips.id"), nullable = False)
  order = db.Column(db.Integer, nullable = True)
  default_destination_id = db.Column(db.Integer,ForeignKey("default_destinations.id"), nullable=True)
  custom_destination_id = db.Column(db.Integer, ForeignKey("custom_destinations.id"),nullable=True)
  start = db.Column(db.DateTime, nullable=True)
  end = db.Column(db.DateTime, nullable=True)
  distance = db.Column(db.Integer, nullable=True)

  default_destinations = relationship("Default_destination", back_populates="events")
  custom_destinations = relationship("Custom_destination", back_populates="events")
  trips = relationship("Trip", back_populates="events")


  def to_dict(self):
    return {
      "id": self.id,
      "trip_id": self.trip_id,
      "order":self.order,
      "default_destination_id": self.default_destination_id,
      "custom_destination_id": self.custom_destination_id,
      "start": self.start,
      "end": self.end,
      "distance": self.distance,
      "title": self.custom_destinations.name if self.custom_destinations else self.default_destinations.name,
      "name": self.custom_destinations.name if self.custom_destinations else self.default_destinations.name,
      "duration": self.default_destinations.duration if self.default_destinations else self.custom_destinations.duration,
      "lat": self.default_destinations.lat if self.default_destinations else self.custom_destinations.lat,
      "lng": self.default_destinations.lng if self.default_destinations else self.custom_destinations.lng,
      "image_url": self.default_destinations.image_url if self.default_destinations else self.custom_destinations.image_url

    }


  def to_dict_wo_ll(self):
    return {
      "id": self.id,
      "order":self.order,
      "start": self.start,
      "end": self.end,

    }

