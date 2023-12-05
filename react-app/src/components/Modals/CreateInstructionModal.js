import React, { useEffect, useState } from "react";
import { useModal } from '../../context/Modal'
import { useDispatch, useSelector } from "react-redux";
import "./EditCollectionModal.css"
import { createRecipeInstructionThunk } from "../../store/recipeInstruction";

function AddInstructionModal({ recipeId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [desc, setDesc] = useState("")
    const [instructionNum, setInstructionNum] = useState(null)
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});

        const payload = {
            recipe_id: recipeId,
            desc: desc,
            instruction_num: parseInt(instructionNum)
        };

        const res = await dispatch(createRecipeInstructionThunk(payload))

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
                <h1>Add Instruction</h1>

                <label>
                    Instruction
                    {errors.desc && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.desc}</p>
                    )}
                    <input
                        type="text"
                        placeholder="instruction"
                        value={desc}
                        onChange={(e) => setDesc(e.target.value)}
                    />
                </label>

                <label>
                    Instruction Number
                    {errors.instructionNum && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.instructionNum}</p>
                    )}
                    <input
                        type="number"
                        placeholder="instruction number"
                        value={instructionNum}
                        onChange={(e) => setInstructionNum(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!desc || !instructionNum}
                >Add Instruction</button>
            </form>
        </div>
    )
}

export default AddInstructionModal;
