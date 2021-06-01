from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class City(db.Model):
  __tablename__ = 'cities'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(40), nullable = False)
  image_url = db.Column(db.String, nullable = True)
  coutry_id = db.Column(db.Integer, ForeignKey('countries.id'), nullable = False)

  countries = relationship("Country", back_populates="cities")
  trips = relationship("Trip", back_populates="cities")
  custom_destinations = relationship("Custom_destination", back_populates="cities")
  default_destinations = relationship("Default_destination", back_populates="cities")

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "coutry_id": self.coutry_id
    }

