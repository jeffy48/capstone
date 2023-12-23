from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Collection, db, CollectionRecipe, Recipe, User
from app.forms import CollectionForm, CollectionRecipeForm
from app.api.user_routes import user_routes

collection_routes = Blueprint('collections', __name__)

@collection_routes.route("/<int:collection_id>")
def get_collection(collection_id):
    collection = db.session.query(Collection, User).join(User, Collection.user_id == User.id).filter(Collection.id == collection_id).one()
    collectionObj = {}
    collectionObj.update(collection[0].to_dict())
    collectionObj.update(collection[1].to_dict_username())
    return collectionObj

@collection_routes.route('/')
def get_all_collections():
    collections = db.session.query(Collection, User).join(User, Collection.user_id == User.id).filter(Collection.public == True).all()
    res = []
    for i in range(len(collections)):
        collectionsObj = {}
        collectionsObj.update(collections[i][0].to_dict())
        collectionsObj.update(collections[i][1].to_dict_username())
        res.append(collectionsObj)
    return res

@user_routes.route('/<int:user_id>/collections')
@login_required
def get_user_collections(user_id):
    """
    Query for a user's collections by user_id and returns them in a list of collection dictionaries
    """
    collections = Collection.query.filter_by(user_id=user_id).all()
    return jsonify([collection.to_dict() for collection in collections])

@user_routes.route('/<int:user_id>/collectionrecipes')
@login_required
def get_user_collection_recipes(user_id):
    """
    Query for a user's collections by user_id and returns them in a list of collection dictionaries
    """
    collections = db.session.query(Collection, CollectionRecipe).join(CollectionRecipe, Collection.id == CollectionRecipe.collection_id).filter(Collection.user_id == user_id).all()
    res = []
    for i in range(len(collections)):
        collectionsObj = {}
        collectionsObj.update(collections[i][0].to_dict())
        collectionsObj.update(collections[i][1].to_dict_collection())
        res.append(collectionsObj)
    return res

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
    if collection:
        db.session.delete(collection)
        db.session.commit()
        return collection.to_dict()
    return {'errors': "Deletion failed: Collection not found"}, 404
