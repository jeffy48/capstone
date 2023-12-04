import React, { useEffect, useState } from "react";
import { updateCollectionThunk } from "../../store/collection";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import "./EditCollectionModal.css"

function EditCollectionModal({ collectionId, userId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [name, setName] = useState("")
    const [privacy, setPrivacy] = useState(null)
    const [desc, setDesc] = useState("")
    const [errors, setErrors] = useState({})

    const handleEdit = async (event) => {
        event.preventDefault();
        setErrors({});
        let payloadPrivacy;

        payloadPrivacy = privacy === "true";

        const payload = {
            user_id: userId,
            name: name,
            desc: desc,
            // need payloadPrivacy to convert string to bool
            public: payloadPrivacy
        };

        const res = await dispatch(updateCollectionThunk(collectionId, payload))

        console.log("hi", res)

        if (res.errors) {
            // res.errors is object with keys of fieldnames and values of arrays, each index being an error string
            setErrors(res.errors);
            console.log(errors.name)
        } else {
            closeModal()
        };
    }

    // const handleClick = () => {
    //     closeModal();
    // }

    return (
        <div className="create-recipe">
            <form className="recipe-form" onSubmit={handleEdit}>
                <h1>Edit Collection</h1>

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
                >Edit Collection</button>
            </form>
        </div>
    )
}

export default EditCollectionModal;
