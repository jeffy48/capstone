import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createRecipeThunk } from "../../store/recipe";

function CreateRecipePage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session.user)
    const [name, setName] = useState("")
    const [servings, setServings] = useState(null)
    const [preptime, setPreptime] = useState(null)
    const [cooktime, setCooktime] = useState(null)
    const [difficulty, setDifficulty] = useState("")
    const [privacy, setPrivacy] = useState(null)
    const [image, setImage] = useState("")
    const [errors, setErrors] = useState([])

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors();

        const payload = {
            user_id: user.id,
            name: name,
            servings: servings,
            preptime: preptime,
            cooktime: cooktime,
            difficulty: difficulty,
            public: privacy,
            image: image
        };

        console.log(payload)

        const res = await dispatch(createRecipeThunk(payload));
        console.log(res)
        if (res) {
            setErrors(res.errors);
            console.log(errors)
        } else {
            history.push('/myrecipes')
        };
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h1>Create a New Recipe</h1>

                <label>
                    Recipe Name
                    {/* {errors.name &&
                    <p>{errors.name}</p>
                    } */}
                    <input
                        type="text"
                        placeholder="Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>

                <label>
                    Servings
                    <input
                        type="number"
                        placeholder="Servings"
                        value={servings}
                        onChange={(e) => setServings(e.target.value)}
                    />
                </label>

                <label>
                    Preptime
                    <input
                        type="number"
                        placeholder="Preptime"
                        value={preptime}
                        onChange={(e) => setPreptime(e.target.value)}
                    />
                </label>

                <label>
                    Cooktime
                    <input
                        type="number"
                        placeholder="Cooktime"
                        value={cooktime}
                        onChange={(e) => setCooktime(e.target.value)}
                    />
                </label>

                <label>
                    Difficulty
                    <select required onChange={(e) => setDifficulty(e.target.value)} value={difficulty}>
                        <option value="">--Please choose an option</option>
                        <option value="Easy">Easy</option>
                        <option value="Medium">Medium</option>
                        <option value="Hard">Hard</option>
                    </select>
                </label>

                <label>
                    Public
                    <select required onChange={(e) => setPrivacy(e.target.value)} value={privacy}>
                        <option value="">--Please choose an option</option>
                        <option value={true}>Public</option>
                        <option value={false}>Private</option>
                    </select>
                </label>

                <label>
                    Image
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
                >Create Recipe</button>
            </form>
        </div>
    );
};

export default CreateRecipePage;
