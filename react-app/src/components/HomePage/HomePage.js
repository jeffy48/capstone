import "./HomePage.css"
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllRecipesThunk } from "../../store/recipe"
import { NavLink, useHistory } from "react-router-dom"
import glIcon from "../../images/shopping-list.png"
import collectionIcon from "../../images/bookmark.png"
import reviewIcon from "../../images/five-stars.png"

function HomePage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const allRecipes = useSelector(state => state.recipe.allRecipes);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        dispatch(getAllRecipesThunk());
    }, [dispatch])

    // change to -3 later
    const recentRecipes = allRecipes.slice(3, 6);
    console.log(recentRecipes)

    return (
        <div className="home">

            <div className="home-banner">
                <h1>Cookbook</h1>
            </div>

            <div className="home-recipe">
                <h1>Explore Our Recipes or Create Your Own</h1>
                <div className="home-recipe-container">
                    {recentRecipes.map(recipe => (
                        <NavLink
                            key={recipe.id}
                            style={{ backgroundImage: `url("${recipe.image}")` }}
                            className="home-recipe-card"
                            to={`/recipes/${recipe.id}`}>
                            <h1 className="home-recipe-card-h1">{recipe.name}</h1>
                        </NavLink>
                    ))}
                </div>
            </div>

            <div className="home-info">
                <div className="home-review">
                    <h1>Write Reviews for Recipes</h1>
                    <img className="home-review-icon"
                        src={reviewIcon}
                        alt='review-icon'/>
                </div>

                <div className="home-collection">
                    <h1>Create a Collection of Recipes</h1>
                    <img className="home-collection-icon"
                        src={collectionIcon}
                        alt='collection-icon'/>
                </div>

                <div className="home-gl">
                    <h1>Add Ingredients to a Grocery List</h1>
                    <img className="home-gl-icon"
                        src={glIcon}
                        alt='gl-icon'/>
                </div>
            </div>

            {!user && (
            <div className="home-user">
                <h1>Login or Sign Up</h1>
                <button onClick={() => history.push("/login")}>Join</button>
            </div>
            )}

            <div className="home-banner-2"/>

            <div className="home-credits">
                <a href="https://www.pexels.com/photo/kitchen-knife-on-table-349609/">Photo by Lukas</a>
                <a href="https://www.flaticon.com/free-icons/cookbook" title="cookbook icons">Cookbook icons created by Us and Up - Flaticon</a>
                <a href="https://www.flaticon.com/free-icons/shopping-list" title="shopping list icons">Shopping list icons created by IconBaandar - Flaticon</a>
                <a href="https://www.flaticon.com/free-icons/collection" title="collection icons">Collection icons created by Pixel perfect - Flaticon</a>
                <a href="https://www.flaticon.com/free-icons/five-stars" title="five stars icons">Five stars icons created by bastian 5 - Flaticon</a>
            </div>

        </div>
    )
}

export default HomePage;
