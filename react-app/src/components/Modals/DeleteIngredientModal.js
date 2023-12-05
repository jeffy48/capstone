import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import { deletedRecipeIngredientThunk } from "../../store/recipeIngredient";

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
            <button onClick={handleDelete}>Yes (Delete)</button>
            <button onClick={handleClick}>No (Keep)</button>
        </div>
    )
}

export default DeleteIngredientModal;
