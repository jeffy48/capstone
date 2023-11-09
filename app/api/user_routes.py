from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Recipe

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
