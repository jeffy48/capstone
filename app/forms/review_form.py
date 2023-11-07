from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange

class ReviewForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired(message="user_id is required and must be an integer")])
    recipe_id = IntegerField('recipe_id', validators=[DataRequired(message="recipe_id is required and must be an integer"), Length(min=2, max=50, message="length of name is invalid")])
    content = StringField('content', validators=[DataRequired(message="content is required and must be a string")])
    rating = DecimalField('rating', validators=[DataRequired(message="rating is required and must be an number"), NumberRange(min=1, max=5, message="rating must be between 1 and 5")])
