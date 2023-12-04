import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCollectionsThunk, getUserCollectionsThunk } from "../../store/collection";
import { NavLink, useHistory } from "react-router-dom";

function MyCollectionsPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector(state => state.session.user)
    const userId = user ? user.id : null;
    const userCollections = useSelector(state => state.collection.userCollections)

    useEffect(() => {
        dispatch(getUserCollectionsThunk(userId))
    }, [dispatch])

    if (!user) {
        history.push("/login")
    }

    return (
        <div id="all-collections-page">
            <h1>Explore My Collections</h1>
            <NavLink style={{marginBottom:5}} exact to='/collections'>All Collections</NavLink>
            <NavLink exact to="/collections/create">Create a Collection</NavLink>
            <div className="collection-wrapper">
                {userCollections.map(collection => (
                    <NavLink
                        key={collection.id}
                        className="collection-row"
                        to={`/collections/${collection.id}`}>
                        <h1>{collection.name}</h1>
                        <p>Curated By: {user.username}</p>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default MyCollectionsPage;
