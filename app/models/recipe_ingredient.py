from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeIngredient(db.Model):
  __tablename__ = 'recipe_ingredients'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
  name = db.Column(db.String(25), nullable=False)
  quantity = db.Column(db.Numeric(scale=2), nullable=False)
  measurement = db.Column(db.String(25), nullable=False)
  desc = db.Column(db.String(50), nullable=True)

  recipe = db.relationship('Recipe', back_populates='recipe_ingredients')
  user_grocery_list_ingredients = db.relationship('UserGroceryListIngredient', back_populates='recipe_ingredient', cascade="all, delete-orphan")

  def to_dict(self):
    return {
      'id': self.id,
      'recipe_id': self.recipe_id,
      'name': self.name,
      'quantity': self.quantity,
      'measurement': self.measurement,
      'desc': self.desc
    }

  def to_dict_grocery(self):
    return {
      'ingredient_id': self.id,
      'ingredient_recipe_id': self.recipe_id,
      'ingredient_name': self.name,
      'ingredient_quantity': self.quantity,
      'ingredient_measurement': self.measurement,
      'ingredient_desc': self.desc
    }
