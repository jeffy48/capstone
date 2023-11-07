from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class RecipeInstructionForm(FlaskForm):
    recipe_id = IntegerField('recipe_id', validators=[DataRequired(message="recipe_id is required and must be an integer")])
    desc = StringField('desc', validators=[DataRequired(message="desc is required and must be a string")])
    instruction_num = IntegerField('instruction_num', validators=[DataRequired(message="instruction_num is required and must be an integer")])
