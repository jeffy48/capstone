from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeInstruction(db.Model):
  __tablename__ = 'recipe_instructions'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
  desc = db.Column(db.String(255), nullable=False)
  instruction_num = db.Column(db.Integer, nullable=False)

  recipe = db.relationship('Recipe', back_populates='recipe_instructions')

  def to_dict(self):
    return {
      'id': self.id,
      'recipe_id': self.recipe_id,
      'desc': self.desc,
      'instruction_num': self.instruction_num
    }
