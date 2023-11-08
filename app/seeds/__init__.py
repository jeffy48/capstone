from flask.cli import AppGroup
from .users import seed_users, undo_users
from .recipes import seed_recipes, undo_recipes
from .recipe_ingredients import seed_recipe_ingredients, undo_recipe_ingredients
from .collection_recipes import seed_collection_recipes, undo_collection_recipes
from .collections import seed_collections, undo_collections
from .recipe_instructions import seed_recipe_instructions, undo_recipe_instructions
from .reviews import seed_reviews, undo_reviews
from .user_grocery_list_ingredients import seed_user_grocery_list_ingredients, undo_user_grocery_list_ingredients

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_user_grocery_list_ingredients()
        undo_recipe_instructions()
        undo_recipe_ingredients()
        undo_collection_recipes()
        undo_collections()
        undo_reviews()
        undo_recipes()
        undo_users()
    seed_users()
    seed_recipes()
    seed_reviews()
    seed_collections()
    seed_collection_recipes()
    seed_recipe_ingredients()
    seed_recipe_instructions()
    seed_user_grocery_list_ingredients()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_user_grocery_list_ingredients()
    undo_recipe_instructions()
    undo_recipe_ingredients()
    undo_collection_recipes()
    undo_collections()
    undo_reviews()
    undo_recipes()
    undo_users()
    # Add other undo functions here
