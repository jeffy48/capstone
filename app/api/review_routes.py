from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Review, db
from app.forms import ReviewForm
from app.api.user_routes import user_routes

review_routes = Blueprint('reviews', __name__)

@user_routes.route('/<int:id>/reviews')
@login_required
def get_user_reviews(id):
    """
    A logged in user can get all reviews they've created
    """
    reviews = Review.query.filter_by(user_id=id).all()
    return jsonify([review.to_dict() for review in reviews])

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
