from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, RecipeIngredient
from app.forms import RecipeIngredientForm
from app.api.recipe_routes import recipe_routes

ingredient_routes = Blueprint('ingredients', __name__)

@recipe_routes.route('/<int:recipe_id>/ingredients')
def get_recipe_ingredients(recipe_id):
    """
    Get recipe ingredients by recipe_id
    """
    ingredients = RecipeIngredient.query.filter_by(recipe_id=recipe_id).all()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

@ingredient_routes.route('/', methods=['POST'])
@login_required
def create_recipe_ingredients():
    """
    A logged in user can create a new recipe ingredient for a recipe they own using recipe_id
    """
    form = RecipeIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = RecipeIngredient(
            recipe_id = form.data['recipe_id'],
            name = form.data['name'],
            quantity = form.data['quantity'],
            measurement = form.data['measurement'],
            desc = form.data['desc']
        )
        db.session.add(ingredient)
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': form.errors}, 400

@ingredient_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_recipe_ingredient(id):
    """
    A logged in user can edit a recipe ingredient for a recipe they own using *removed(recipe_id)* and ingredient_id
    """
    form = RecipeIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = RecipeIngredient.query.get(id)
        ingredient.name = form.data['name']
        ingredient.quantity = form.data['quantity'] if form.data['quantity'] is not None else None
        ingredient.measurement = form.data['measurement']
        ingredient.desc = form.data['desc']
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': form.errors}, 400

@ingredient_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe_ingredient(id):
    """
    A logged in user can delete a recipe ingredient for a recipe they own using ingredient_id
    """
    ingredient = RecipeIngredient.query.get(id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()

        return ingredient.to_dict()

    return {'errors': "Deletion failed: Ingredient not found"}, 404
