from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User



class CreateDestinationsForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    city_id = IntegerField('city_id', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    image_url = StringField('image_url', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    duration = IntegerField('duration', validators=[DataRequired()])