import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllRecipesThunk } from "../../../store/recipe"
import './AllRecipesPage.css'
import defaultImage from "../../../images/default.jpg"

function AllRecipesPage() {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const allRecipes = useSelector(state => state.recipe.allRecipes);

    useEffect(() => {
        dispatch(getAllRecipesThunk());
    }, [dispatch])

    const getDefaultImage = (img) => {
        img.target.src = defaultImage;
    };

    return (
        <div id="all-recipes-page">
            <h1>Explore All Recipes</h1>
            {user && (
            <NavLink exact to='/myrecipes'>My Recipes</NavLink>
            )}
            <div className="recipe-wrapper">
                {allRecipes.map(recipe => (
                    <NavLink
                        key={recipe.id}
                        to={`/recipes/${recipe.id}`}>
                        <div className="recipe-card">
                            <img
                                onError={getDefaultImage}
                                className="recipe-img"
                                src={recipe.image}
                                alt='recipe-thumbnail-image'
                                title={recipe.name}/>
                            <h1>{recipe.name}</h1>
                            <p>Serves {recipe.servings}</p>
                            <p>Takes {recipe.preptime + recipe.cooktime} minutes</p>
                            <p>Difficulty: {recipe.difficulty}</p>
                        </div>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default AllRecipesPage;
