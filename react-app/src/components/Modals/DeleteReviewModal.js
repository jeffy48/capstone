import { useHistory } from "react-router-dom";
import { deleteReviewThunk } from "../../store/review";
import { useModal } from '../../context/Modal'
import { useDispatch } from "react-redux";

function DeleteReviewModal({ reviewId }) {
    const history = useHistory()
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleDelete = () => {
        dispatch(deleteReviewThunk(reviewId))
        closeModal();
        // history.push("/myreviews")
    }

    const handleClick = () => {
        closeModal();
    }

    return (
        <div>
            <h1>Confirm Delete:</h1>
            <h1>Are you sure you want to remove this review?</h1>
            <button onClick={handleDelete}>Yes (Delete)</button>
            <button onClick={handleClick}>No (Keep)</button>
        </div>
    )
}

export default DeleteReviewModal;
