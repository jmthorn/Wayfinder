from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Default_destination(db.Model):
  __tablename__ = 'default_destinations'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(300), nullable = False)
  city_id = db.Column(db.Integer, ForeignKey("cities.id"), nullable=False)
  description = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=False)
  address = db.Column(db.String, nullable=False)
  lat = db.Column(db.Float, nullable=False)
  lng = db.Column(db.Float, nullable=False)
  duration = db.Column(db.Integer, nullable=False)

  cities = relationship("City", back_populates="default_destinations")
  events = relationship("Event", back_populates="default_destinations")


  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "city_id": self.city_id,
      "description": self.description,
      "image_url": self.image_url,
      "address": self.address,
      "duration": self.duration,
      "lat": self.lat,
      "lng":self.lng

    }
