from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, RecipeInstruction
from app.forms import RecipeInstructionForm
from app.api.recipe_routes import recipe_routes

instruction_routes = Blueprint('instructions', __name__)

@recipe_routes.route('/<int:recipe_id>/instructions')
def get_recipe_instructions(recipe_id):
    """
    Get recipe instructions by recipe_id
    """
    instructions = RecipeInstruction.query.filter_by(recipe_id=recipe_id).all()
    return jsonify([instruction.to_dict() for instruction in instructions])

@instruction_routes.route('/', methods=['POST'])
@login_required
def create_recipe_instruction():
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

@instruction_routes.route('/<int:id>', methods=['PUT'])
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

@instruction_routes.route('/<int:id>', methods=['DELETE'])
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
