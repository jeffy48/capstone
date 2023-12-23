from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import  db, CollectionRecipe, Recipe, Collection, User
from app.forms import CollectionRecipeForm
from app.api.collection_routes import collection_routes

collection_recipe_routes = Blueprint('collection-recipes', __name__)

@collection_routes.route('/<int:collection_id>/recipes')
def get_collection_recipes(collection_id):
    """
    Get all recipes by collection id
    """
    recipes = db.session.query(CollectionRecipe, Recipe, Collection, User).join(Recipe, CollectionRecipe.recipe_id == Recipe.id).join(Collection, CollectionRecipe.collection_id == Collection.id).join(User, Collection.user_id == User.id).filter(CollectionRecipe.collection_id == collection_id).all()
    res = []
    for i in range(len(recipes)):
        recipeObj = {}
        recipeObj.update(recipes[i][0].to_dict())
        recipeObj.update(recipes[i][1].to_dict_collections())
        recipeObj.update(recipes[i][2].to_dict_collections())
        recipeObj.update(recipes[i][3].to_dict_username())
        res.append(recipeObj)
    return res

@collection_recipe_routes.route('/')
@login_required
def create_collection_recipe():
    """
    A logged in user can add a recipe to a collection
    """
    form = CollectionRecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        collection_recipe = CollectionRecipe(
            collection_id = form.data['collection_id'],
            recipe_id = form.data['recipe_id']
        )
        db.session.add(collection_recipe)
        db.session.commit()

        return collection_recipe.to_dict()
    return {'errors': form.errors}, 400

@collection_recipe_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_collection_recipe(id):
    """
    A logged in user can remove a recipe from a collection they own
    """
    collection_recipe = CollectionRecipe.query.get(id)
    if collection_recipe:
        db.session.delete(collection_recipe)
        db.session.commit()
        return collection_recipe.to_dict()
    return {'errors': "Deletion failed: Recipe not found in collection"}, 404
