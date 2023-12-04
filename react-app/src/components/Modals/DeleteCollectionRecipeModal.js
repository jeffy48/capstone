import { useHistory } from "react-router-dom";
import { deleteCollectionRecipeThunk } from "../../store/collectionRecipe";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import "./DeleteCollectionRecipeModal.css"

function DeleteCollectionRecipeModal({ collectionRecipeId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deleteCollectionRecipeThunk(collectionRecipeId))
        closeModal();
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Removal:</h1>
            <h1>Are you sure you want to remove this recipe from the collection?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Remove)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteCollectionRecipeModal;
