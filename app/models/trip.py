from .db import db


class Trip(db.Model):
  __tablename__ = 'trips'

  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, nullable = False)
  city_id = db.Column(db.Integer, nullable = False)
  start_date = db.Column(db.Date, nullable = False)
  end_date = db.Column(db.Date, nullable = False)


  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "city_id": self.city_id,
      "start_date": self.start_date,
      "end_date": self.end_date
    }
