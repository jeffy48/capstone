from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, AnyOf

class CollectionForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired(message="user_id is required and must be an integer")])
    name = StringField('name', validators=[DataRequired(message="name is required and must be a string"), Length(min=2, max=75, message="length of name is invalid")])
    desc = StringField('desc', validators=[DataRequired(message="desc is required and must be an string")])
    public = BooleanField('public', validators=[AnyOf([True, False])])
