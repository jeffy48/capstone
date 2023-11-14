from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Collection, db, CollectionRecipe, Recipe
from app.forms import CollectionForm, CollectionRecipeForm
from app.api.user_routes import user_routes

collection_routes = Blueprint('collections', __name__)

# do i need a get all collections and get a collection if im not going to use it? (would it be considered full crud if i only return a 'read' for get all user collections instead)

# maybe nest this blueprint in collection_routes.py instead? is there a better way to write this route?
@user_routes.route('/<int:user_id>/collections')
@login_required
def get_user_collections(user_id):
    """
    Query for a user's collections by user_id and returns them in a list of collection dictionaries
    """
    collections = Collection.query.filter_by(user_id=user_id).all()
    return jsonify([collection.to_dict() for collection in collections])

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