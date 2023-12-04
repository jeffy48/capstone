const GET_COLLECTION_RECIPES = 'collectionRecipe/GET_COLLECTION_RECIPES';
const CREATE_COLLECTION_RECIPE = 'collectionRecipe/CREATE_COLLECTION_RECIPE';
const DELETE_COLLECTION_RECIPE = 'collectionRecipe/DELETE_COLLECTION_RECIPE';

const getCollectionRecipes = (collectionRecipes) => ({
	type: GET_COLLECTION_RECIPES,
	payload: collectionRecipes
});

const createCollectionRecipe = (collectionRecipe) => ({
	type: CREATE_COLLECTION_RECIPE,
	payload: collectionRecipe
});

const deleteCollectionRecipe = (collectionRecipe) => ({
	type: DELETE_COLLECTION_RECIPE,
	payload: collectionRecipe
})

export const getCollectionRecipesThunk = (collectionId) => async dispatch => {
	const res = await fetch(`/api/collections/${collectionId}/recipes`);
	try {
		const collectionRecipes = await res.json();
		dispatch(getCollectionRecipes(collectionRecipes));
	}
	catch(error) {
		return error
	}
};

export const createCollectionRecipeThunk = (payload) => async dispatch => {
	const res = await fetch('/api/collection-recipes', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
	try {
        const collectionRecipe = await res.json()
        dispatch(createCollectionRecipe(collectionRecipe))
    }
    catch(error) {
        return error
    }
};

export const deleteCollectionRecipeThunk = (collectionRecipeId) => async dispatch => {
	const res = await fetch(`/api/collection-recipes/${collectionRecipeId}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
	});
	try {
        const collectionRecipe = await res.json()
        dispatch(deleteCollectionRecipe(collectionRecipe))
    }
    catch(error) {
        return error
    }
};

const initialState = { collectionRecipes: [], createdCollectionRecipe: {}, deletedCollectionRecipe: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_COLLECTION_RECIPES:
            return {...state, collectionRecipes: action.payload}
		case CREATE_COLLECTION_RECIPE:
			return {...state, createdCollectionRecipe: action.payload}
		case DELETE_COLLECTION_RECIPE:
			return {...state, deletedCollectionRecipe: action.payload}
		default:
			return state;
	}
};
