from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Recipe, Collection, Review, UserGroceryListIngredient, RecipeIngredient, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

# maybe nest this blueprint in recipe_routes.py instead? is there a better way to write this route?
@user_routes.route('/<int:user_id>/recipes')
@login_required
def get_user_recipes(user_id):
    """
    Query for a user's recipes by user_id and returns them in a list of recipe dictionaries
    """
    recipes = Recipe.query.filter_by(user_id=user_id).all()
    return jsonify([recipe.to_dict() for recipe in recipes])

# maybe nest this blueprint in collection_routes.py instead? is there a better way to write this route?
@user_routes.route('/<int:user_id>/collections')
@login_required
def get_user_collections(user_id):
    """
    Query for a user's collections by user_id and returns them in a list of collection dictionaries
    """
    collections = Collection.query.filter_by(user_id=user_id).all()
    return jsonify([collection.to_dict() for collection in collections])

@user_routes.route('/<int:id>/reviews')
@login_required
def get_user_reviews(id):
    """
    A logged in user can get all reviews they've created
    """
    reviews = Review.query.filter_by(user_id=id).all()
    return jsonify([review.to_dict() for review in reviews])

@user_routes.route('/<int:id>/grocery_list')
@login_required
def get_user_grocery_list(id):
    """
    A logged in user can get all the recipe ingredients in their grocery list
    """
    grocery_list = db.session.query(UserGroceryListIngredient, RecipeIngredient).join(RecipeIngredient, UserGroceryListIngredient.recipe_ingredient_id == RecipeIngredient.id).filter(UserGroceryListIngredient.user_id == id).all()
    res = [ingredient[1] for ingredient in grocery_list]

    return jsonify([ingredient.to_dict() for ingredient in res])
