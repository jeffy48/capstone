from .db import db, environment, SCHEMA, add_prefix_for_prod

class UserGroceryListIngredient(db.Model):
  __tablename__ = 'user_grocery_list_ingredients'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  recipe_ingredient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipe_ingredients.id")), nullable=False)
  checked = db.Column(db.Boolean, nullable=False)

  user = db.relationship('User', back_populates='user_grocery_list_ingredients')
  recipe_ingredient = db.relationship('RecipeIngredient', back_populates='user_grocery_list_ingredients')


  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'recipe_ingredient_id': self.recipe_ingredient_id,
      'checked': self.checked
    }
