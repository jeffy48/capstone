import { useHistory } from "react-router-dom";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import { deleteCollectionThunk } from "../../store/collection";
import "./DeleteCollectionRecipeModal.css"

function DeleteCollectionModal({ collectionId }) {
    const dispatch = useDispatch()
    const history = useHistory();
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deleteCollectionThunk(collectionId))
        closeModal();
        history.push("/mycollections")
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this collection?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Delete)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteCollectionModal;
