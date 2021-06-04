from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Trip(db.Model):
  __tablename__ = 'trips'

  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer,ForeignKey("users.id"), nullable = False)
  city_id = db.Column(db.Integer, ForeignKey("cities.id"),nullable = False)
  start_date = db.Column(db.DateTime, nullable = False)
  end_date = db.Column(db.DateTime, nullable = False)

  users = relationship("User", back_populates="trips")
  cities = relationship("City", back_populates="trips")
  events = relationship("Event", cascade="all, delete", back_populates="trips")

  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "city_id": self.city_id,
      "start_date": self.start_date,
      "end_date": self.end_date,
      "image_url": self.cities.image_url,
      "name": self.cities.name
    }
  def to_dict_wo_cities(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "city_id": self.city_id,
      "start_date": self.start_date,
      "end_date": self.end_date
    }



