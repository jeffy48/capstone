from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CollectionRecipeForm(FlaskForm):
    collection_id = IntegerField('collection_id', validators=[DataRequired(message="collection_id is required and must be an integer")])
    recipe_id = IntegerField('recipe_id', validators=[DataRequired(message="recipe_id is required and must be an integer")])
