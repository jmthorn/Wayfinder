from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey



class Country(db.Model):
  __tablename__ = 'countries'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  cities = relationship("City", back_populates="countries")

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
    }

