import React, { useState } from "react";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import "./EditCollectionModal.css"
import { createRecipeIngredientThunk } from "../../store/recipeIngredient";

function AddIngredientModal({ recipeId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [name, setName] = useState("")
    const [quantity, setQuantity] = useState(null)
    const [measurement, setMeasurement] = useState("")
    const [desc, setDesc] = useState("")
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});

        const payload = {
            recipe_id: recipeId,
            name: name,
            quantity: quantity,
            measurement: measurement,
            desc: desc
        };

        const res = await dispatch(createRecipeIngredientThunk(payload))

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
                <h1>Add Ingredient</h1>

                <label>
                    Ingredient Name
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
                        placeholder="Quantity"
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                    />
                </label>

                <label>
                    Unit of Measurement
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
                    Description (optional)
                    {errors.desc && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.desc}</p>
                    )}
                    <input
                        type="text"
                        placeholder="ex. diced"
                        value={desc}
                        onChange={(e) => setDesc(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!name || !quantity || !measurement}
                >Add Ingredient</button>
            </form>
        </div>
    )
}

export default AddIngredientModal;
