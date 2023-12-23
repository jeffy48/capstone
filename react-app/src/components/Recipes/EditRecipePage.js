import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from 'react-router-dom'
import { getRecipeThunk } from "../../store/recipe";
import { getRecipeIngredientsThunk } from "../../store/recipeIngredient";
import { getRecipeInstructionsThunk } from "../../store/recipeInstruction";
import { getRecipeReviewsThunk } from "../../store/review";
import "./RecipePage.css"
import defaultImage from "../../images/default.jpg"
import OpenModalButton from "../Modals/OpenModalButton";
import EditRecipeModal from "../Modals/EditRecipeModal";
import AddIngredientModal from "../Modals/CreateIngredientModal";
import DeleteIngredientModal from "../Modals/DeleteIngredientModal";
import AddInstructionModal from "../Modals/CreateInstructionModal";
import DeleteInstructionModal from "../Modals/DeleteInstructionModal";
import "./EditRecipePage.css"
import DeleteRecipeModal from "../Modals/DeleteRecipeModal";
import EditIngredientModal from "../Modals/EditIngredientModal";
import EditInstructionModal from "../Modals/EditInstructionModal";

function EditRecipePage() {
    const dispatch = useDispatch()
    const history = useHistory();
    const { recipeId } = useParams();
    const user = useSelector(state => state.session.user);
    const userId = user ? user.id : null;
    const recipe = useSelector(state => state.recipe.recipe);
    const ingredients = useSelector(state => state.recipeIngredient.recipeIngredients)
    const instructions = useSelector(state => state.recipeInstruction.recipeInstructions)
    const reviews = useSelector(state => state.review.recipeReviews)

    useEffect(() => {
        dispatch(getRecipeThunk(recipeId));
        dispatch(getRecipeIngredientsThunk(recipeId))
        dispatch(getRecipeInstructionsThunk(recipeId))
        dispatch(getRecipeReviewsThunk(recipeId))
    }, [dispatch])


    if (instructions.length > 0 && !recipe.public && recipe.user_id !== userId) {
        return (
            <h1 style={{color:"red"}}>403 Unauthorized: Not owner of private recipe</h1>
        )
    }

    const getDefaultImage = (img) => {
        img.target.src = defaultImage;
    };

    const sortedInstructions = instructions.sort((a, b) => a.instruction_num > b.instruction_num ? 1 : -1)

    console.log(ingredients)

    return (
        <div className="recipe-page">
            <div className="recipe-page-container">
                <div className="recipe-about">
                    <h1>{recipe.name}</h1>
                    <div className="recipe-info">
                        <p>Servings: {recipe.servings}</p>
                        <p>Preptime: {recipe.preptime} minutes</p>
                        <p>Cooktime: {recipe.cooktime} minutes</p>
                        <p>Difficulty: {recipe.difficulty}</p>
                    </div>
                    <h2>Posted by: {recipe.username}</h2>
                    <OpenModalButton
                    buttonText="Edit Recipe Info"
                    modalComponent={<EditRecipeModal recipeId={recipe.id} userId={userId} />}
                    />
                </div>
                <img onError={getDefaultImage} src={recipe.image}/>
                <div className="recipe-instructions">
                    <h1>Ingredients:</h1>
                    {/* map through recipe ingredients with 2 columns */}
                    {ingredients.map(ingredient => (
                        <div style={{display: "flex", columnGap:15, marginBottom:20}}>
                            <li className="recipe-ingredient-container">{ingredient.quantity ? parseFloat(ingredient.quantity).toFixed(2) : null} {ingredient.measurement} {ingredient.name} {ingredient.desc && (`(${ingredient.desc})`)}</li>
                            <div className="edit-recipe-ingr-container">
                                <OpenModalButton
                                    className="edit-recipe-ingr-buttons"
                                    buttonText="-"
                                    modalComponent={<DeleteIngredientModal ingredientId={ingredient.id}/>}
                                />
                                <OpenModalButton
                                    className="edit-recipe-ingr-buttons"
                                    buttonText="Edit"
                                    modalComponent={<EditIngredientModal ingredientId={ingredient.id} recipeId={recipeId} />}
                                />
                            </div>
                        </div>
                    ))}
                    <OpenModalButton
                    className="edit-recipe-ingr-buttons"
                    buttonText="Add Ingredient"
                    modalComponent={<AddIngredientModal recipeId={recipe.id} />}
                    />
                </div>
                <div className="recipe-ingredients">
                    <h1>Instructions:</h1>
                    {/* map through recipe intructions */}
                    {sortedInstructions.map(instruction => (
                        <div style={{display: "flex", columnGap:15}}>
                            <p className="recipe-ingredient-container">{instruction.instruction_num}. {instruction.desc}</p>
                            <div className="edit-recipe-ingr-container">
                                <OpenModalButton
                                    style={{height:20, alignSelf:"center"}}
                                    className="edit-recipe-ingr-buttons"
                                    buttonText="-"
                                    modalComponent={<DeleteInstructionModal instructionId={instruction.id} />}
                                />
                                <OpenModalButton
                                        className="edit-recipe-ingr-buttons"
                                        buttonText="Edit"
                                        modalComponent={<EditInstructionModal instructionId={instruction.id} recipeId={recipeId} />}
                                />
                            </div>
                        </div>
                    ))}
                    <OpenModalButton
                    className="edit-recipe-ingr-buttons"
                    buttonText="Add Instruction"
                    modalComponent={<AddInstructionModal recipeId={recipe.id} />}
                    />
                </div>
                <OpenModalButton
                    className="delete-recipe"
                    buttonText="Delete Recipe"
                    modalComponent={<DeleteRecipeModal recipeId={recipe.id}/>}
                    />
            </div>
        </div>
    )
}

export default EditRecipePage;
