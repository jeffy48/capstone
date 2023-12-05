from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Review, db, User, Recipe
from app.forms import ReviewForm
from app.api.user_routes import user_routes
from app.api.recipe_routes import recipe_routes

review_routes = Blueprint('reviews', __name__)

@recipe_routes.route('/<int:recipe_id>/reviews')
def get_recipe_reviews(recipe_id):
    """
    Get all reviews for a recipe
    """
    # reviews = Review.query.filter_by(recipe_id=recipe_id).all()
    # return jsonify([review.to_dict() for review in reviews])
    reviews = db.session.query(Review, User).join(User, Review.user_id == User.id).filter(Review.recipe_id == recipe_id).all()
    res = []
    for i in range(len(reviews)):
        reviewObj = {}
        reviewObj.update(reviews[i][0].to_dict())
        reviewObj.update(reviews[i][1].to_dict_username())
        res.append(reviewObj)
    return res

@user_routes.route('/<int:user_id>/reviews')
@login_required
def get_user_reviews(user_id):
    """
    A logged in user can get all reviews they've created
    """
    reviews = db.session.query(Review, User, Recipe).join(User, Review.user_id == User.id).join(Recipe, Review.recipe_id == Recipe.id).filter(Review.user_id == user_id).all()
    res = []
    print(reviews)
    for i in range(len(reviews)):
        reviewObj = {}
        reviewObj.update(reviews[i][0].to_dict())
        reviewObj.update(reviews[i][1].to_dict_username())
        reviewObj.update(reviews[i][2].to_dict_name())
        res.append(reviewObj)
    return res
    # reviews = Review.query.filter_by(user_id=user_id).all()
    # return jsonify([review.to_dict() for review in reviews])

@review_routes.route('/', methods=['POST'])
def create_review():
    """
    A logged in user can create a new review for a recipe
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            user_id = form.data['user_id'],
            recipe_id = form.data['recipe_id'],
            content = form.data['content'],
            rating = form.data['rating']
        )
        db.session.add(review)
        db.session.commit()

        return review.to_dict()
    return {'errors': form.errors}, 400

@review_routes.route('/<int:id>', methods=['PUT'])
def update_review(id):
    """
    A logged in user can edit a review they own for a recipe
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review.query.get(id)
        review.content = form.data['content']
        review.rating = form.data['rating']
        db.session.commit()

        return review.to_dict()
    return {'errors': form.errors}, 400

@review_routes.route('/<int:id>', methods=['DELETE'])
def delete_review(id):
    """
    A logged in user can delete a review they own for a recipe
    """
    review = Review.query.get(id)
    if review:
        db.session.delete(review)
        db.session.commit()
        return review.to_dict()
    return {'errors': "Deletion failed: Collection not found"}, 404
