import React, { useEffect, useState } from "react";
import { updateCollectionThunk } from "../../store/collection";
import { useModal } from '../../context/Modal'
import { useDispatch, useSelector } from "react-redux";
import "./EditCollectionModal.css"
import { updateRecipeThunk } from "../../store/recipe";
import { useParams } from 'react-router-dom'
import { updateRecipeIngredientThunk } from "../../store/recipeIngredient";

function EditIngredientModal({ ingredientId, recipeId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [name, setName] = useState("")
    const [quantity, setQuantity] = useState("")
    const [measurement, setMeasurement] = useState("")
    const [desc, setDesc] = useState("")
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});

        const payload = {
            recipe_id: recipeId,
            name: name,
            measurement: measurement,
            desc: desc
        };

        if (quantity !== "") {
            payload.quantity = quantity;
        }

        const res = await dispatch(updateRecipeIngredientThunk(payload, ingredientId))

        console.log("hi", payload)

        if (res.errors) {
            // res.errors is object with keys of fieldnames and values of arrays, each index being an error string
            setErrors(res.errors);
            console.log(errors.name)
        } else {
            closeModal()
        };
    }

    return (
        <div className="create-recipe">
            <form className="recipe-form" onSubmit={handleSubmit}>
                <h1>Edit Ingredient</h1>

                <label>
                    Ingredient Name*
                    {errors.name && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.name}</p>
                    )}
                    <input
                        type="text"
                        placeholder="Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>

                <label>
                    Quantity
                    {errors.quantity && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.quantity}</p>
                    )}
                    <input
                        type="number"
                        placeholder="Servings"
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                    />
                </label>

                <label>
                    Unit of Measurement*
                    {errors.measurement && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.measurement}</p>
                    )}
                    <input
                        type="text"
                        placeholder="ex. tbsp"
                        value={measurement}
                        onChange={(e) => setMeasurement(e.target.value)}
                    />
                </label>

                <label>
                    Description
                    {errors.desc && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.desc}</p>
                    )}
                    <input
                        type="text"
                        placeholder="desc"
                        value={desc}
                        onChange={(e) => setDesc(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!name || !measurement}
                >Edit Ingredient</button>
                <p style={{margin:0, fontSize:12}}>* (required)</p>
            </form>
        </div>
    )
}

export default EditIngredientModal;
