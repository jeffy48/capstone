import { deleteReviewThunk } from "../../store/review";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";
import "./DeleteCollectionRecipeModal.css"

function DeleteReviewModal({ reviewId }) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deleteReviewThunk(reviewId))
        closeModal();
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this review?</h1>
            <div>
                <button onClick={handleDelete}>Yes (Delete)</button>
                <button onClick={handleClick}>No (Keep)</button>
            </div>
        </div>
    )
}

export default DeleteReviewModal;
