import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useParams } from "react-router-dom";
import { getCollectionRecipesThunk } from "../../store/collectionRecipe";
import { getCollectionThunk } from "../../store/collection";
import './CollectionPage.css'
import defaultImage from "../../images/default.jpg"
import EditCollectionModal from "../EditCollectionModal";
import OpenModalButton from "../OpenModalButton";

function CollectionPage() {
    const dispatch = useDispatch()
    const { collectionId } = useParams();
    const user = useSelector(state => state.session.user)
    const userId = user ? user.id : null
    const collectionRecipes = useSelector(state => state.collectionRecipe.collectionRecipes);
    const collection = useSelector(state => state.collection.collection)

    useEffect(() => {
        dispatch(getCollectionThunk(collectionId))
        dispatch(getCollectionRecipesThunk(collectionId))
    }, [dispatch, collectionId])

    const getDefaultImage = (img) => {
        img.target.src = defaultImage;
    };

    return (
        <div id="all-collections-page">
            <div className="collection-about-container">
                <h1 style={{ marginBottom:5 }}>{collection.name}</h1>
                <h2 style={{ marginTop:5, fontSize: 20 }}>Curated By: {collection.username}</h2>
                <p>{collection.desc}</p>
                {userId === collection.user_id && (
                    <OpenModalButton
                    buttonText="Edit"
                    modalComponent={<EditCollectionModal collectionId={collection.id} userId={userId} />}
                    />
                )}
            </div>
            <h1 style={{ marginTop:25, fontSize: 24, marginBottom:0, textDecoration: "underline" }}>Recipes in this Collection:</h1>
            <div className="recipe-wrapper">
                {collectionRecipes.length > 0 ? collectionRecipes.map(recipe => (
                    <NavLink
                        key={recipe.id}
                        to={`/recipes/${recipe.id}`}>
                        <div className="recipe-card">
                            <img
                                onError={getDefaultImage}
                                className="recipe-img"
                                src={recipe.recipe_image}
                                alt='recipe-thumbnail-image'
                                title={recipe.recipe_name}/>
                            <h1>{recipe.recipe_name}</h1>
                            <p>Serves {recipe.recipe_servings}</p>
                            <p>Takes {recipe.recipe_preptime + recipe.recipe_cooktime} minutes</p>
                            <p>Difficulty: {recipe.recipe_difficulty}</p>
                            {/* {userId === recipe.collection_user_id && (
                                <OpenModalButton
                                buttonText="Delete"
                                modalComponent={<DeleteCollectionRecipeModal collectionRecipeId={recipe.id} />}
                            />
                            )} */}

                        </div>
                    </NavLink>
                ))
                : <h1>No recipes in this collection</h1>}
            </div>
        </div>
    )
}

export default CollectionPage;
