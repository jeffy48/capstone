from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange, AnyOf, Length

class RecipeForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired(message="user_id is required and must be an integer")])
    name = StringField('name', validators=[DataRequired(message="name is required and must be a string"), Length(min=2, max=50, message="length of name is invalid")])
    preptime = IntegerField('preptime', validators=[DataRequired(message="preptime is required and must be an integer"), NumberRange(min=1, message="preptime must be greater 0 minutes")])
    difficulty = StringField('difficulty', validators=[DataRequired(message="difficulty is required and must be a string of 'Easy', 'Medium', or 'Hard'"), AnyOf(['Easy', 'Medium', 'Hard' ])])
    public = BooleanField('public', validators=[DataRequired(message="public is required and must be a boolean")])
    image = StringField('image', validators=[DataRequired(message="image is required and must be a url string")])
