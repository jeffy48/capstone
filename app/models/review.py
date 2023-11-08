from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
  __tablename__ = 'reviews'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
  content = db.Column(db.String, nullable=False)
  rating = db.Column(db.Numeric(scale=1), nullable=False)

  user = db.relationship('User', back_populates='reviews')
  recipe = db.relationship('Recipe', back_populates='reviews')

  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'recipe_id': self.recipe_id,
      'content': self.content,
      'rating': self.rating
    }
