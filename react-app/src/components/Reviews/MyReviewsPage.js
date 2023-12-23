import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, NavLink } from "react-router-dom";
import { getUserReviewsThunk } from "../../store/review";
import OpenModalButton from "../Modals/OpenModalButton";
import DeleteReviewModal from "../Modals/DeleteReviewModal";
import './MyReviewsPage.css'

function MyReviewsPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session.user);
    const userId = user ? user.id : null;


    useEffect(() => {
        dispatch(getUserReviewsThunk(userId))
    }, [dispatch])

    const reviews = useSelector(state => state.review.userReviews)

    if (!user) {
        history.push("/login")
    }

    const myReviews = reviews.slice();

    console.log(myReviews)

    const handleEdit = () => {
        // open modal for editreviewmodal
    }

    return (
        <div className="review-page">
            <div className="review-container">
                <h1>My Reviews</h1>
                {myReviews.length > 0 ? myReviews.map(review => (
                    <div id={review.id}  className="review">
                        <NavLink to={`/recipes/${review.recipe_id}`}>Review for {review.recipe_name}</NavLink>
                        <p>Rating: {review.rating} / 5</p>
                        <p>{`"${review.content}"`}</p>
                        {/* <button>Edit</button>
                        <OpenModalButton
                            buttonText="Delete"
                            modalComponent={<DeleteReviewModal reviewId={review.id} />}
                        /> */}
                    </div>
                ))
                : <h1 style={{marginTop:25, fontSize: 22}}>You do not have any reviews at the moment.</h1>}
            </div>
        </div>
    )
}

export default MyReviewsPage;
