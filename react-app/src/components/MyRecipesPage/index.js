import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getUserRecipesThunk } from "../../store/recipe";

function MyRecipesPage() {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user);
    // was getting typeerror: reading undefined null for id. code below will set the id variable after checking if user is not null
    const userId = user ? user.id : null;
    const userRecipes = useSelector(state => state.recipe.userRecipes);

    useEffect(() => {
        dispatch(getUserRecipesThunk(userId));
    }, [dispatch])

    return (
        <div id="all-recipes-page">
            <h1>Your Recipes</h1>
            <div className="recipe-wrapper">
                {userRecipes.map(recipe => (
                    <NavLink
                        key={recipe.id}
                        className="recipe-card"
                        to={'/recipes'}>
                        <img
                            className="recipe-img"
                            src={recipe.image}
                            alt='recipe-thumbnail-image'
                            title={recipe.name}/>
                        <h1>{recipe.name}</h1>
                        <p>Serves {recipe.servings}</p>
                        <p>Takes {recipe.preptime + recipe.cooktime} minutes</p>
                        <p>Difficulty: {recipe.difficulty}</p>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default MyRecipesPage;
