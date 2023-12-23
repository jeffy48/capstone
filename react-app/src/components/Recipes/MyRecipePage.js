import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { getUserRecipesThunk } from "../../store/recipe";
import defaultImage from "../../images/default.jpg"

function MyRecipesPage() {
    const dispatch = useDispatch()
    const history = useHistory();
    const user = useSelector(state => state.session.user);
    // was getting typeerror: reading undefined null for id. code below will set the id variable after checking if user is not null
    const userId = user ? user.id : null;
    const userRecipes = useSelector(state => state.recipe.userRecipes);

    useEffect(() => {
        dispatch(getUserRecipesThunk(userId));
    }, [dispatch])

    if (!user) {
        history.push("/login")
    }

    const getDefaultImage = (img) => {
        img.target.src = defaultImage;
    };

    return (
        <div id="all-recipes-page">
            <h1>Your Recipes</h1>
            <NavLink exact to="/recipes" style={{marginBottom:5}}>Recipes</NavLink>
            <NavLink exact to="/recipes/create">Create a Recipe</NavLink>
            <div className="recipe-wrapper">
                {userRecipes.length > 0 ? userRecipes.map(recipe => (
                    <NavLink
                        key={recipe.id}
                        className="recipe-card"
                        to={`/recipes/${recipe.id}`}>
                        <img
                            onError={getDefaultImage}
                            className="recipe-img"
                            src={recipe.image}
                            alt='recipe-thumbnail'
                            title={recipe.name}/>
                        <h1>{recipe.name}</h1>
                        <p>Serves {recipe.servings}</p>
                        <p>Takes {recipe.preptime + recipe.cooktime} minutes</p>
                        <p>Difficulty: {recipe.difficulty}</p>
                    </NavLink>
                ))
                : <h1 style={{marginTop:25, fontSize: 22}}>You do not have any recipes at the moment.</h1>}
            </div>
        </div>
    )
}

export default MyRecipesPage;
