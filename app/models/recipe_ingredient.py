from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeIngredient(db.Model):
  __tablename__ = 'recipe_ingredients'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
  name = db.Column(db.String(25), nullable=False)
  quantity = db.Column(db.Float, nullable=False)
  measurement = db.Column(db.String(25), nullable=False)
  desc = db.Column(db.String(25), nullable=True)

  recipe = db.relationship('Recipe', back_populates='recipe_ingredients')

  def to_dict(self):
    return {
      'id': self.id,
      'recipe_id': self.recipe_id,
      'name': self.name,
      'quantity': self.quantity,
      'measurement': self.measurement,
      'desc': self.desc
    }