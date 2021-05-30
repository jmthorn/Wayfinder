from .db import db


class Custom_destination(db.Model):
  __tablename__ = 'custom_destinations'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(300), nullable = False)
  city_id = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=False)
  address = db.Column(db.String, nullable=False)
  duration = db.Column(db.Integer, nullable=False)
  user_id = db.Column(db.Integer, nullable=False)


  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "city_id": self.city_id,
      "description": self.description,
      "image_url": self.image_url,
      "address": self.address,
      "duration": self.duration,
      "user_id": self.user_id

    }
