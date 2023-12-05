// import React, { useEffect, useState } from "react";
// import { getUserCollectionRecipesThunk, getUserCollectionsThunk, updateCollectionThunk } from "../../store/collection";
// import { useModal } from '../../context/Modal'
// import { useDispatch, useSelector } from "react-redux";
// import "./EditCollectionModal.css"
// import { updateRecipeThunk } from "../../store/recipe";
// import { useParams } from 'react-router-dom'
// import { createPortal } from "react-dom";

// function AddRecipeToCollectionModal({ recipeId, userId }) {
//     const dispatch = useDispatch()
//     const userCollections = useSelector(state => state.collection.userCollectionRecipes);
//     const { closeModal } = useModal()
//     const [collectionId, setCollectionId] = useState(null)
//     const [errors, setErrors] = useState({})

//     useEffect(() => {
//         dispatch(getUserCollectionRecipesThunk(userId))
//         console.log(userCollections)
//     }, [dispatch])

//     const filteredCollections = userCollections.filter(collection => collection.recipe_id !== recipeId)

//     // const handleSubmit = async (event) => {
//     //     event.preventDefault();
//     //     setErrors({});

//     //     const payload = {
//     //         collection_id: collectionId,
//     //         recipe_id: recipeId
//     //     };

//     //     const res = await dispatch(createRecipeIngredientThunk(payload))

//     //     console.log("hi", payload)

//     //     if (res.errors) {
//     //         // res.errors is object with keys of fieldnames and values of arrays, each index being an error string
//     //         setErrors(res.errors);
//     //         console.log(errors.name)
//     //     } else {
//     //         closeModal()
//     //     };
//     // }

//     return (
//         <form>
//             {filteredCollections.map(collection => (
//                 <div>
//                     <input type="checkbox" id={collection.id} name={collection.id} onChange={(e) => handleCheckBoxChange(collection.)}/>
//                     <label for={collection.id}>{collection.name}</label>
//                 </div>
//             ))}

//         </form>
//     )
// }

// export default AddRecipeToCollectionModal;
