import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllRecipesThunk } from "../../../store/recipe"
import './AllRecipesPage.css'

function AllRecipesPage() {
    const dispatch = useDispatch()
    const allRecipes = useSelector(state => state.recipe.allRecipes);

    useEffect(() => {
        dispatch(getAllRecipesThunk());
    }, [dispatch])

    return (
        <div id="all-recipes-page">
            <h1>Explore All Recipes</h1>
            <div className="recipe-wrapper">
                {allRecipes.map(recipe => (
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

export default AllRecipesPage;
