import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createCollectionThunk } from "../../store/collection";

function CreateCollectionPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session.user)
    const [name, setName] = useState("")
    const [privacy, setPrivacy] = useState(null)
    const [desc, setDesc] = useState("")
    const [errors, setErrors] = useState({})

    if (!user) {
        history.push("/login")
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors({});
        let payloadPrivacy;

        payloadPrivacy = privacy === "true";

        const payload = {
            user_id: user.id,
            name: name,
            desc: desc,
            // need payloadPrivacy to convert string to bool
            public: payloadPrivacy
        };

        console.log(payload)

        const res = await dispatch(createCollectionThunk(payload));
        // res is recipe obj on success and object w key errors on failure
        console.log(res)
        if (res.errors) {
            // res.errors is object with keys of fieldnames and values of arrays, each index being an error string
            setErrors(res.errors);
            console.log(errors.name)
        } else {
            history.push('/mycollections')
        };
    };

    return (
        <div className="create-recipe">
            <form className="recipe-form" onSubmit={handleSubmit}>
                <h1>Create a New Collection</h1>

                <label>
                    Collection Name
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

                <button
                    type="submit"
                    disabled={!name || !(privacy !== "") || !desc}
                >Create Collection</button>
            </form>
        </div>
    );
}

export default CreateCollectionPage;
