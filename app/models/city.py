from .db import db


class City(db.Model):
  __tablename__ = 'cities'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(40), nullable = False, unique = True)
  coutry_id = db.Column(db.Integer, nullable = False, unique = True)


  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "coutry_id": self.coutry_id
    }
