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
import AddRecipeToCollectionModal from "../Modals/AddRecipeToCollectionModal";

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

    const getDefaultImage = (img) => {
        img.target.src = defaultImage;
    };

    const handleEdit = () => {
        history.push(`/recipes/${recipe.id}/edit`)
    }

    const sortedInstructions = instructions.sort((a, b) => a.instruction_num > b.instruction_num ? 1 : -1)

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
                    {userId === recipe.user_id &&
                    <button onClick={handleEdit}>Edit Recipe</button>}
                </div>
                <img onError={getDefaultImage} src={recipe.image}/>
                <div className="recipe-instructions">
                    <h1>Ingredients:</h1>
                    {/* map through recipe ingredients with 2 columns */}
                    {ingredients.map(ingredient => (
                        <li>{ingredient.quantity} {ingredient.measurement} {ingredient.name} {ingredient.desc && (`(${ingredient.desc})`)}</li>
                    ))}
                </div>
                <div className="recipe-ingredients">
                    <h1>Instructions:</h1>
                    {/* map through recipe intructions */}
                    {/* might have to refactor this to check instruction num. rn, it is just assuming instructions from db are in order */}
                    {sortedInstructions.map(instruction => (
                        <p>{instruction.instruction_num}. {instruction.desc}</p>
                    ))}
                </div>
                {/* {user && (
                    <OpenModalButton
                    buttonText="Add Recipe to a Collection"
                    modalComponent={<AddRecipeToCollectionModal recipeId={recipe.id} userId={userId}/>}
                    />
                )} */}
                <div className="recipe-page-reviews">
                    <h1>Reviews</h1>
                    {/* map through recipe reviews */}
                    {reviews.map(review => (
                        <div className="recipe-page-review">
                            <p>User: {review.username}</p>
                            <p>Stars: {review.rating} / 5</p>
                            <p style={{fontStyle:"italic"}}>"{review.content}"</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default RecipePage;
