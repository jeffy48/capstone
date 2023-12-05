from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, UserGroceryListIngredient, RecipeIngredient
from app.forms import UserGroceryListIngredientForm
from app.api.user_routes import user_routes

user_grocery_list_ingredient_routes = Blueprint('grocery-list-ingredients', __name__)

@user_routes.route('/<int:user_id>/grocery-list-ingredients')
@login_required
def get_user_grocery_list(user_id):
    """
    A logged in user can get all the recipe ingredients in their grocery list
    """
    grocery_list = db.session.query(UserGroceryListIngredient, RecipeIngredient).join(RecipeIngredient, UserGroceryListIngredient.recipe_ingredient_id == RecipeIngredient.id).filter(UserGroceryListIngredient.user_id == user_id).all()
    res = []
    for i in range(len(grocery_list)):
        ingredientObj = {}
        ingredientObj.update(grocery_list[i][0].to_dict())
        ingredientObj.update(grocery_list[i][1].to_dict_grocery())
        res.append(ingredientObj)
    return res
    # grocery_list = db.session.query(UserGroceryListIngredient, RecipeIngredient).join(RecipeIngredient, UserGroceryListIngredient.recipe_ingredient_id == RecipeIngredient.id).filter(UserGroceryListIngredient.user_id == user_id).all()
    # res = [ingredient[1] for ingredient in grocery_list]
    # return jsonify([ingredient.to_dict() for ingredient in res])

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

# @user_grocery_list_ingredient_routes.route('/<int:id>', methods=['PUT'])
# @login_required
# def update_grocery_list_ingredient(id):
#     """
#     A logged in user can add a recipe's ingredients to their grocery list
#     """
#     form = UserGroceryListIngredientForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         ingredient = UserGroceryListIngredient(
#             recipe_ingredient_id = form.data['recipe_ingredient_id'],
#             user_id = form.data['user_id'],
#             checked = form.data['checked']
#         )
#         db.session.add(ingredient)
#         db.session.commit()

#         return ingredient.to_dict()
#     return {'errors': form.errors}, 400

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
