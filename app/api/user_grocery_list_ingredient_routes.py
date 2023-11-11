from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, UserGroceryListIngredient, RecipeIngredient
from app.forms import UserGroceryListIngredientForm
from app.api.user_routes import user_routes

user_grocery_list_ingredient_routes = Blueprint('grocery_list', __name__)

@user_routes.route('/<int:id>/grocery_list')
@login_required
def get_user_grocery_list(id):
    """
    A logged in user can get all the recipe ingredients in their grocery list
    """
    grocery_list = db.session.query(UserGroceryListIngredient, RecipeIngredient).join(RecipeIngredient, UserGroceryListIngredient.recipe_ingredient_id == RecipeIngredient.id).filter(UserGroceryListIngredient.user_id == id).all()
    res = [ingredient[1] for ingredient in grocery_list]

    return jsonify([ingredient.to_dict() for ingredient in res])

@user_grocery_list_ingredient_routes.route('/<int:id>', methods=['POST'])
@login_required
def create_grocery_list_ingredient(id):
    """
    A logged in user can add a recipe's ingredients to their grocery list
    """
    form = UserGroceryListIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = UserGroceryListIngredient(
            recipe_ingredient_id = form.data['recipe_ingredient_id'],
            user_id = form.data['user_id'],
            checked = form.data['checked']
        )
        db.session.add(ingredient)
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': form.errors}, 400

@user_grocery_list_ingredient_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_grocery_list_ingredient(id):
    """
    A logged in user can remove a recipe's ingredient from their grocery list
    """
    ingredient = UserGroceryListIngredient.query.get(id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': "Deletion failed: Grocery list ingredient not found"}, 404
