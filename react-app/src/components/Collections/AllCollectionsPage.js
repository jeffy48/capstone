import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCollectionsThunk } from "../../store/collection";
import { NavLink } from "react-router-dom";
import './AllCollectionsPage.css'

function AllCollectionsPage() {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user)
    const allCollections = useSelector(state => state.collection.collections)

    useEffect(() => {
        dispatch(getAllCollectionsThunk())
    }, [dispatch])

    return (
        <div id="all-collections-page">
            <h1>Explore All Collections</h1>
            {user && (
            <NavLink exact to='/mycollections'>My Collections</NavLink>
            )}
            <div className="collection-wrapper">
                {allCollections.map(collection => (
                    <NavLink
                        key={collection.id}
                        className="collection-row"
                        to={`/collections/${collection.id}`}>
                        <h1>{collection.name}</h1>
                        <p>Curated By: {collection.username}</p>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default AllCollectionsPage;
