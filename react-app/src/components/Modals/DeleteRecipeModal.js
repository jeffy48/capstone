import { useHistory } from "react-router-dom";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import { deleteRecipeThunk } from "../../store/recipe";
import "./DeleteCollectionRecipeModal.css"

function DeleteRecipeModal({ recipeId }) {
    const dispatch = useDispatch()
    const history = useHistory();
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deleteRecipeThunk(recipeId))
        closeModal();
        history.push("/myrecipes")
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this recipe?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Delete)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteRecipeModal;
