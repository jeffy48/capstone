from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Recipe, db, User
from app.forms import RecipeForm, RecipeIngredientForm, RecipeInstructionForm
from app.api.user_routes import user_routes

recipe_routes = Blueprint('recipes', __name__)

# maybe add an additional all public recipes route and use that OR use this below and filter in frontend
# maybe get rid of login required since you dont have to be logged in to see all recipes
# maybe add error handler here
@recipe_routes.route('/')
def get_all_recipes():
    """
    Query for all recipes and returns them in a list of recipe dictionaries
    """
    recipes = Recipe.query.filter_by(public=True).all()
    return jsonify([recipe.to_dict() for recipe in recipes])

# maybe nest this blueprint in recipe_routes.py instead? is there a better way to write this route?
@user_routes.route('/<int:user_id>/recipes')
@login_required
def get_user_recipes(user_id):
    """
    Query for a user's recipes by user_id and returns them in a list of recipe dictionaries
    """
    recipes = Recipe.query.filter_by(user_id=user_id).all()
    return jsonify([recipe.to_dict() for recipe in recipes])

# maybe get rid of login required since you dont have to be logged in to see a recipe
# maybe add error handler here
@recipe_routes.route('/<int:id>')
def get_recipe(id):
    """
    Query for one recipe by id and returns recipe dictionary
    """
    # recipe = Recipe.query.get(id)
    # return recipe.to_dict()
    recipe = db.session.query(Recipe, User).join(User, Recipe.user_id == User.id).filter(Recipe.id == id).one()
    res = {}
    res.update(recipe[0].to_dict())
    res.update(recipe[1].to_dict_username())
    print(res)
    return jsonify(res)


@recipe_routes.route('/', methods=['POST'])
@login_required
def create_recipe():
    """
    Creates a new recipe
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe(
            user_id = form.data['user_id'],
            name = form.data['name'],
            servings = form.data['servings'],
            preptime = form.data['preptime'],
            cooktime = form.data['cooktime'],
            difficulty = form.data['difficulty'],
            public = form.data['public'],
            image = form.data['image']
        )
        db.session.add(recipe)
        db.session.commit()

        return recipe.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_recipe(id):
    """
    A logged in user can update their existing recipe by id
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe.query.get(id)
        recipe.name = form.data['name']
        recipe.servings = form.data['servings']
        recipe.preptime = form.data['preptime']
        recipe.cooktime = form.data['cooktime']
        recipe.difficulty = form.data['difficulty']
        recipe.public = form.data['public']
        recipe.image = form.data['image']
        db.session.commit()

        return recipe.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe(id):
    """
    A logged in user can delete their existing recipe by id
    """
    recipe = Recipe.query.get(id)
    # if this doesn't work, change to "if recipe is not None"
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return recipe.to_dict()
    return {'errors': "Deletion failed: Recipe not found"}, 404
