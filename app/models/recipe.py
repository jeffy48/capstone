from .db import db, environment, SCHEMA, add_prefix_for_prod

class Recipe(db.Model):
  __tablename__ = 'recipes'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  preptime = db.Column(db.Integer, nullable=False)
  difficulty = db.Column(db.String(10), nullable=False)
  public = db.Column(db.Boolean)
  image = db.Column(db.String)

  user = db.relationship('User', back_populates='recipes')
  recipe_ingredients = db.relationship('RecipeIngredient', back_populates='recipe', cascade="all, delete-orphan")
  recipe_instructions = db.relationship('RecipeInstruction', back_populates='recipe', cascade="all, delete-orphan")
  collection_recipes = db.relationship('CollectionRecipe', back_populates='recipe', cascade="all, delete-orphan")
  reviews = db.relationship('Review', back_populates='recipe', cascade="all, delete-orphan")


  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'name': self.name,
      'preptime': self.preptime,
      'difficulty': self.difficulty,
      'public': self.public,
      'image': self.image
    }
