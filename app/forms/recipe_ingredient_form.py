from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length

class RecipeIngredientForm(FlaskForm):
    recipe_id = IntegerField('recipe_id', validators=[DataRequired(message="recipe_id is required and must be an integer")])
    name = StringField('name', validators=[DataRequired(message="name is required and must be a string"), Length(min=2, max=25, message="length of name is invalid")])
    quantity = DecimalField('quantity', validators=[DataRequired(message="quantity is required and must be a number"), NumberRange(min=0.01, message="quantity must be greater 0")])
    measurement = StringField('measurement', validators=[DataRequired(message="measurement is required and must be a string"), Length(min=2, max=25, message="length of measurement is invalid")])
    desc = StringField('desc', validators=[Length(max=50, message="length of desc is invalid")])
