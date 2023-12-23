import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import { deletedRecipeIngredientThunk } from "../../store/recipeIngredient";
import "./DeleteCollectionRecipeModal.css"

function DeleteIngredientModal({ ingredientId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deletedRecipeIngredientThunk(ingredientId))
        closeModal();
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this ingredient?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Delete)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteIngredientModal;
