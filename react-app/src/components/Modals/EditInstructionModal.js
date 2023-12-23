import React, { useState } from "react";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import "./EditCollectionModal.css"

import { updateRecipeInstructionThunk } from "../../store/recipeInstruction";

function EditInstructionModal({ instructionId, recipeId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const [desc, setDesc] = useState("")
    const [instructionNum, setInstructionNum] = useState("")
    const [errors, setErrors] = useState({})

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrors({});

        const payload = {
            recipe_id: recipeId,
            desc: desc,
        };

        if (instructionNum !== "") {
            payload.instruction_num = instructionNum;
        }

        const res = await dispatch(updateRecipeInstructionThunk(payload, instructionId))

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
                <h1>Edit Instruction</h1>

                <label>
                    Instruction*
                    {errors.desc && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.desc}</p>
                    )}
                    <input
                        type="text"
                        placeholder="Instruction"
                        value={desc}
                        onChange={(e) => setDesc(e.target.value)}
                    />
                </label>

                <label>
                    Instruction Order Number*
                    {errors.instruction_num && (
                    <p className="create-recipe-error" style={{color:"red"}}>{errors.instruction_num}</p>
                    )}
                    <input
                        type="number"
                        placeholder="ex. 1"
                        value={instructionNum}
                        onChange={(e) => setInstructionNum(e.target.value)}
                    />
                </label>

                <button
                    type="submit"
                    disabled={!desc || !instructionNum}
                >Edit Instruction</button>
                <p style={{margin:0, fontSize:12}}>* (required)</p>
            </form>
        </div>
    )
}

export default EditInstructionModal;
