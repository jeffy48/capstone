from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField
from wtforms.validators import DataRequired

class UserGroceryListIngredientForm(FlaskForm):
    recipe_ingredient_id = IntegerField('recipe_ingredient_id', validators=[DataRequired(message="recipe_ingredient_id is required and must be an integer")])
    user_id = IntegerField('user_id', validators=[DataRequired(message="user_id is required and must be an integer")])
    checked = BooleanField('checked', default=False)
