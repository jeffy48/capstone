from .db import db, environment, SCHEMA, add_prefix_for_prod

class CollectionRecipe(db.Model):
  __tablename__ = 'collection_recipes'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  collection_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("collections.id")), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)

  collection = db.relationship('Collection', back_populates='collection_recipes')
  recipe = db.relationship('Recipe', back_populates='collection_recipes')

  def to_dict(self):
    return {
      'id': self.id,
      'collection_id': self.collection_id,
      'recipe_id': self.recipe_id
    }

  def to_dict_collection(self):
    return {
      'collection_recipe_id': self.id,
      'recipe_id': self.recipe_id
    }
