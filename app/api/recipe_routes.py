from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Recipe, db, RecipeIngredient, RecipeInstruction
from app.forms import RecipeForm, RecipeIngredientForm, RecipeInstructionForm

recipe_routes = Blueprint('recipes', __name__)

# maybe add an additional all public recipes route and use that OR use this below and filter in frontend
# maybe get rid of login required since you dont have to be logged in to see all recipes
# maybe add error handler here
@recipe_routes.route('/')
def get_all_recipes():
    """
    Query for all recipes and returns them in a list of recipe dictionaries
    """
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

# maybe get rid of login required since you dont have to be logged in to see a recipe
# maybe add error handler here
@recipe_routes.route('/<int:id>')
def get_recipe(id):
    """
    Query for one recipe by id and returns recipe dictionary
    """
    recipe = Recipe.query.get(id)
    return recipe.to_dict()

@recipe_routes.route('/', methods=['POST'])
@login_required
def create_recipe():
    """
    Creates a new recipe
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe(
            user_id = form.data['user_id'],
            name = form.data['name'],
            servings = form.data['servings'],
            preptime = form.data['preptime'],
            cooktime = form.data['cooktime'],
            difficulty = form.data['difficulty'],
            public = form.data['public'],
            image = form.data['image']
        )
        db.session.add(recipe)
        db.session.commit()

        return recipe.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_recipe(id):
    """
    A logged in user can update their existing recipe by id
    """
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe.query.get(id)
        recipe.name = form.data['name']
        recipe.servings = form.data['servings']
        recipe.preptime = form.data['preptime']
        recipe.cooktime = form.data['cooktime']
        recipe.difficulty = form.data['difficulty']
        recipe.public = form.data['public']
        recipe.image = form.data['image']
        db.session.commit()

        return recipe.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe(id):
    """
    A logged in user can delete their existing recipe by id
    """
    recipe = Recipe.query.get(id)
    # if this doesn't work, change to "if recipe is not None"
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return recipe.to_dict()
    return {'errors': "Deletion failed: Recipe not found"}, 404

# maybe get rid of login required since you dont have to be logged in to see a recipe's ingredients
# maybe add error handler here
# should recipe ingredients and instructions be in another route file? maybe nest the blueprints? could make it more readable
@recipe_routes.route('/<int:id>/ingredients')
def get_recipe_ingredients(id):
    """
    Get recipe ingredients by recipe_id
    """
    ingredients = RecipeIngredient.query.filter_by(recipe_id=id).all()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

# should recipe ingredients and instructions be in another route file? maybe nest the blueprints? could make it more readable
@recipe_routes.route('/<int:recipe_id>/ingredients', methods=['POST'])
@login_required
def create_recipe_ingredients(recipe_id):
    """
    A logged in user can create a new recipe ingredient for a recipe they own using recipe_id
    """
    form = RecipeIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = RecipeIngredient(
            recipe_id = form.data['recipe_id'],
            name = form.data['name'],
            quantity = form.data['quantity'],
            measurement = form.data['measurement'],
            desc = form.data['desc']
        )
        db.session.add(ingredient)
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': form.errors}, 400

# should recipe ingredients and instructions be in another route file? maybe nest the blueprints? could make it more readable
# do i need both params here, or only ingredient_id
@recipe_routes.route('/ingredients/<int:id>', methods=['PUT'])
@login_required
def update_recipe_ingredient(id):
    """
    A logged in user can edit a recipe ingredient for a recipe they own using *removed(recipe_id)* and ingredient_id
    """
    form = RecipeIngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = RecipeIngredient.query.get(id)
        ingredient.name = form.data['name']
        ingredient.quantity = form.data['quantity']
        ingredient.measurement = form.data['measurement']
        ingredient.desc = form.data['desc']
        db.session.commit()

        return ingredient.to_dict()
    return {'errors': form.errors}, 400

# should recipe ingredients and instructions be in another route file? maybe nest the blueprints? could make it more readable
# do i need both params here, or only ingredient_id
@recipe_routes.route('/ingredients/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe_ingredient(id):
    """
    A logged in user can delete a recipe ingredient for a recipe they own using ingredient_id
    """
    ingredient = RecipeIngredient.query.get(id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()

        return ingredient.to_dict()

    return {'errors': "Deletion failed: Ingredient not found"}, 404

@recipe_routes.route('/<int:id>/instructions')
def get_recipe_instructions(id):
    """
    Get recipe instructions by recipe_id
    """
    instructions = RecipeInstruction.query.filter_by(recipe_id=id).all()
    return jsonify([instruction.to_dict() for instruction in instructions])

@recipe_routes.route('/<int:id>/instructions', methods=['POST'])
@login_required
def create_recipe_instruction(recipe_id):
    """
    A logged in user can create a new recipe instruction for a recipe they own
    """
    form = RecipeInstructionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        instruction = RecipeInstruction(
            recipe_id = form.data['recipe_id'],
            desc = form.data['desc'],
            instruction_num = form.data['instruction_num']
        )
        db.session.add(instruction)
        db.session.commit()

        return instruction.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/instructions/<int:id>', methods=['PUT'])
@login_required
def update_recipe_instruction(id):
    """
    A logged in user can edit a recipe instruction for a recipe they own
    """
    form = RecipeInstructionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        instruction = RecipeInstruction.query.get(id)
        instruction.desc = form.data['desc']
        instruction.instruction_num = form.data['instruction_num']
        db.session.commit()

        return instruction.to_dict()
    return {'errors': form.errors}, 400

@recipe_routes.route('/instructions/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe_instruction(id):
    """
    A logged in user can delete a recipe instruction for a recipe they own
    """
    instruction = RecipeInstruction.query.get(id)
    if instruction:
        db.session.delete(instruction)
        db.session.commit()

        return instruction.to_dict()

    return {'errors': "Deletion failed: Instruction not found"}, 404
