import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import { deletedRecipeIngredientThunk } from "../../store/recipeIngredient";
import { deletedRecipeInstructionThunk } from '../../store/recipeInstruction';
import "./DeleteCollectionRecipeModal.css"

function DeleteInstructionModal({ instructionId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deletedRecipeInstructionThunk(instructionId))
        closeModal();
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this instruction?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Delete)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteInstructionModal;
