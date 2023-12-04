import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from 'react-router-dom'
import { getRecipeThunk } from "../../store/recipe";
import { getRecipeIngredientsThunk } from "../../store/recipeIngredient";
import { getRecipeInstructionsThunk } from "../../store/recipeInstruction";
import { getRecipeReviewsThunk } from "../../store/review";

function RecipePage() {
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

    return (
        <div className="recipe-page">
            <div>
                <div>
                    <h1>{recipe.name}</h1>
                    <h2>Posted by: {recipe.username}</h2>
                </div>
                <img src={recipe.image}/>
            </div>
            <div>
                <p>Serves: {recipe.servings}</p>
                <p>Preptime: {recipe.preptime}</p>
                <p>Cooktime: {recipe.cooktime}</p>
                <p>Difficulty: {recipe.difficulty}</p>
            </div>
            <div>
                <h1>Ingredients:</h1>
                {/* map through recipe ingredients with 2 columns */}
                {ingredients.map(ingredient => (
                    <li>{ingredient.quantity} {ingredient.measurement} {ingredient.name} {ingredient.desc && (`(${ingredient.desc})`)}</li>
                ))}
            </div>
            <div>
                <h1>Instructions:</h1>
                {/* map through recipe intructions */}
                {/* might have to refactor this to check instruction num. rn, it is just assuming instructions from db are in order */}
                {instructions.map(instruction => (
                    <p>{instruction.instruction_num}. {instruction.desc}</p>
                ))}
            </div>
            <div>
                <h1>Reviews</h1>
                {/* map through recipe reviews */}
                {reviews.map(review => (
                    <div>
                        <p>{review.username}</p>
                        <p>{review.rating}</p>
                        <p>{review.content}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default RecipePage;
