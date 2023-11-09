from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Collection, db, CollectionRecipe, Recipe
from app.forms import CollectionForm, CollectionRecipeForm

collection_routes = Blueprint('collection', __name__)

# do i need a get all collections and get a collection if im not going to use it? (would it be considered full crud if i only return a 'read' for get all user collections instead)

@collection_routes.route('/', methods=['POST'])
@login_required
def create_collection():
    """
    A logged in user can create a new collection
    """
    form = CollectionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        collection = Collection(
            user_id = form.data['user_id'],
            name = form.data['name'],
            desc = form.data['desc'],
            public = form.data['public']
        )
        db.session.add(collection)
        db.session.commit()

        return collection.to_dict()
    return {'errors': form.errors}, 400

@collection_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_collection(id):
    """
    A logged in user can edit an existing collection they own
    """
    form = CollectionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        collection = Collection.query.get(id)
        collection.name = form.data['name']
        collection.desc = form.data['desc']
        collection.public = form.data['public']
        db.session.commit()

        return collection.to_dict()
    return {'errors': form.errors}, 400

@collection_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_collection(id):
    """
    A logged in user can delete an existing collection they own
    """
    collection = Collection.query.get(id)
    # if this doesn't work, change to "if collection is not None"
    if collection:
        db.session.delete(collection)
        db.session.commit()
        return collection.to_dict()
    return {'errors': "Deletion failed: Collection not found"}, 404

@collection_routes.route('/<int:id>/recipes')
@login_required
def get_collection_recipes(id):
    """
    Get all recipes by collection id
    """
    recipes = db.session.query(CollectionRecipe, Recipe).join(Recipe, CollectionRecipe.recipe_id == Recipe.id).filter(CollectionRecipe.collection_id == id).all()
    res = [recipe[1] for recipe in recipes]

    return jsonify([recipe.to_dict() for recipe in res])

@collection_routes.route('/<int:id>/recipes')
@login_required
def create_collection_recipe(id):
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

@collection_routes.route('/<int:collection_id>/recipes/<int:recipe_id>', methods=['DELETE'])
@login_required
def delete_collection_recipe(collection_id, recipe_id):
    """
    A logged in user can remove a recipe from a collection they own
    """
    collection_recipe = CollectionRecipe.query.filter_by(collection_id=collection_id, recipe_id=recipe_id).one()
    if collection_recipe:
        db.session.delete(collection_recipe)
        db.session.commit()
        return collection_recipe.to_dict()
    return {'errors': "Deletion failed: Recipe not found in collection"}, 404
