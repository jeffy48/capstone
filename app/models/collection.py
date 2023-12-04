from .db import db, environment, SCHEMA, add_prefix_for_prod

class Collection(db.Model):
  __tablename__ = 'collections'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  name = db.Column(db.String(75), nullable=False)
  desc = db.Column(db.String, nullable=False)
  public = db.Column(db.Boolean, nullable=False)

  user = db.relationship('User', back_populates='collections')
  collection_recipes = db.relationship('CollectionRecipe', back_populates='collection', cascade="all, delete-orphan")

  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'name': self.name,
      'desc': self.desc,
      'public': self.public
    }

  def to_dict_collections(self):
    return {
      'collection_user_id': self.user_id,
      'collection_name': self.name,
      'collection_desc': self.desc,
      'collection_public': self.public
    }
