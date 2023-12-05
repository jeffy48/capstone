import React, { useEffect, useState } from "react";
import { updateCollectionThunk } from "../../store/collection";
import { useModal } from '../../context/Modal'
import { useDispatch, useSelector } from "react-redux";
import "./EditCollectionModal.css"
import { updateRecipeThunk } from "../../store/recipe";
import { useParams } from 'react-router-dom'

function EditRecipeModal({ recipeId, userId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [name, setName] = useState("")
    const [servings, setServings] = useState(null)
    const [preptime, setPreptime] = useState(null)
    const [cooktime, setCooktime] = useState(null)
    const [difficulty, setDifficulty] = useState("")
    const [privacy, setPrivacy] = useState(null)
    const [image, setImage] = useState("")
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});
        let payloadPrivacy;

        payloadPrivacy = privacy === "true";

        const payload = {
            user_id: userId,
            name: name,
            servings: servings,
            preptime: preptime,
            cooktime: cooktime,
            difficulty: difficulty,
            // need payloadPrivacy to convert string to bool
            public: payloadPrivacy,
            image: image
        };

        const res = await dispatch(updateRecipeThunk(recipeId, payload))

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
                <h1>Edit Recipe</h1>

                <label>
                    Recipe Name
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
                    Servings
                    {errors.servings && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.servings}</p>
                    )}
                    <input
                        type="number"
                        placeholder="Servings"
                        value={servings}
                        onChange={(e) => setServings(e.target.value)}
                    />
                </label>

                <label>
                    Preptime
                    {errors.preptime && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.preptime}</p>
                    )}
                    <input
                        type="number"
                        placeholder="(minutes)"
                        value={preptime}
                        onChange={(e) => setPreptime(e.target.value)}
                    />
                </label>

                <label>
                    Cooktime
                    {errors.cooktime && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.cooktime}</p>
                    )}
                    <input
                        type="number"
                        placeholder="(minutes)"
                        value={cooktime}
                        onChange={(e) => setCooktime(e.target.value)}
                    />
                </label>

                <label>
                    Difficulty
                    {errors.difficulty && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.difficulty}</p>
                    )}
                    <select required onChange={(e) => setDifficulty(e.target.value)} value={difficulty}>
                        <option value="">--Please choose an option</option>
                        <option value="Easy">Easy</option>
                        <option value="Medium">Medium</option>
                        <option value="Hard">Hard</option>
                    </select>
                </label>

                <label>
                    Public
                    {errors.public && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.public}</p>
                    )}
                    <select required onChange={(e) => setPrivacy(e.target.value)} value={privacy}>
                        <option value="">--Please choose an option</option>
                        <option value={true}>Public</option>
                        <option value={false}>Private</option>
                    </select>
                </label>

                <label>
                    Image
                    {errors.image && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.image}</p>
                    )}
                    <input
                        type="text"
                        placeholder="Image URL"
                        value={image}
                        onChange={(e) => setImage(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!name || !servings || !preptime || !cooktime || !difficulty || !(privacy !== "") || !image}
                >Edit Recipe</button>
            </form>
        </div>
    )
}

export default EditRecipeModal;
