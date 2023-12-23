import React, { useEffect, useState } from "react";
import { updateCollectionThunk } from "../../store/collection";
import { useModal } from '../../context/Modal'
import { useDispatch, useSelector } from "react-redux";
import { updateRecipeThunk } from "../../store/recipe";
import { useParams } from 'react-router-dom'
import { createRecipeIngredientThunk } from "../../store/recipeIngredient";
import { createReviewThunk } from "../../store/review";

function CreateReviewModal({ recipeId, userId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [content, setContent] = useState("")
    const [rating, setRating] = useState("")
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});

        const payload = {
            user_id: userId,
            recipe_id: recipeId,
            content: content,
            rating: rating
        };

        const res = await dispatch(createReviewThunk(payload))

        console.log("hi", payload)

        if (res.errors) {
            // res.errors is object with keys of fieldnames and values of arrays, each index being an error string
            setErrors(res.errors);
        } else {
            closeModal()
        };
    }

    return (
        <div className="create-recipe">
            <form className="recipe-form" onSubmit={handleSubmit}>
                <h1>Create a Review</h1>

                <label>
                    Review*
                    {errors.content && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.content}</p>
                    )}
                    <input
                        style={{width:450, height: 150}}
                        type="text"
                        placeholder="review for recipe"
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                    />
                </label>

                <label>
                    Rating*
                    {errors.rating && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.rating}</p>
                    )}
                    <input
                        type="number"
                        placeholder="ex. 1"
                        value={rating}
                        onChange={(e) => setRating(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!content || !rating}
                >Create Review</button>
            </form>
        </div>
    )
}

export default CreateReviewModal;
