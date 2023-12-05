const GET_RECIPE_INGREDIENTS = 'recipeIngredient/GET_RECIPE_INGREDIENTS';
const CREATE_RECIPE_INGREDIENT = 'recipeIngredient/CREATE_RECIPE_INGREDIENT';
const UPDATE_RECIPE_INGREDIENT = 'recipeIngredient/UPDATE_RECIPE_INGREDIENT';
const DELETE_RECIPE_INGREDIENT = 'recipeIngredient/DELETE_RECIPE_INGREDIENT';

const getRecipeIngredients = (ingredients) => ({
	type: GET_RECIPE_INGREDIENTS,
	payload: ingredients
});

const createRecipeIngredient = (ingredient) => ({
	type: CREATE_RECIPE_INGREDIENT,
	payload: ingredient
});

const updateRecipeIngredient = (ingredient) => ({
	type: UPDATE_RECIPE_INGREDIENT,
	payload: ingredient
});

const deleteRecipeIngredient = (ingredientId) => ({
	type: DELETE_RECIPE_INGREDIENT,
	payload: ingredientId
})

export const getRecipeIngredientsThunk = (recipeId) => async dispatch => {
	const res = await fetch(`/api/recipes/${recipeId}/ingredients`);
	try {
		const ingredients = await res.json();
		dispatch(getRecipeIngredients(ingredients));
	}
	catch(error) {
		return error
	}
};

export const createRecipeIngredientThunk = (payload) => async dispatch => {
	const res = await fetch('/api/ingredients/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
	try {
        const ingredient = await res.json()
        dispatch(createRecipeIngredient(ingredient))
		return ingredient
    }
    catch(error) {
        return error
    }
};

export const updateRecipeIngredientThunk = (payload, id) => async dispatch => {
	const res = await fetch(`/api/ingredients/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
	});
	try {
        const ingredient = await res.json()
        dispatch(updateRecipeIngredient(ingredient))
		return ingredient
    }
    catch(error) {
        return error
    }
};

export const deletedRecipeIngredientThunk = (id) => async dispatch => {
	const res = await fetch(`/api/ingredients/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
	});
	try {
        const ingredient = await res.json()
        dispatch(deleteRecipeIngredient(ingredient.id))
    }
    catch(error) {
        return error
    }
};

const initialState = { recipeIngredients: [], createdIngredient: {}, updatedIngredient: {}, deletedIngredient: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_RECIPE_INGREDIENTS:
            return {...state, recipeIngredients: action.payload}
		case CREATE_RECIPE_INGREDIENT:
			return {...state, createdIngredient: action.payload, recipeIngredients: [...state.recipeIngredients, action.payload]}
		case UPDATE_RECIPE_INGREDIENT:
			const updatedRecipeIngredients = state.recipeIngredients.map(ingredient => {
				// Check if the current ingredient has the same id as the updated ingredient
				if (ingredient.id === action.payload.id) {
					// If yes, replace it with the updated ingredient
					return action.payload;
				}
				// If not, keep the current ingredient unchanged
				return ingredient;
			});
			return {...state, recipeIngredients: updatedRecipeIngredients, updatedIngredient: action.payload}
		case DELETE_RECIPE_INGREDIENT:
			const updatedIngredients = state.recipeIngredients.filter(ingredient => ingredient.id !== action.payload)
			return {...state, recipeIngredients: updatedIngredients, deletedIngredient: action.payload}
		default:
			return state;
	}
};
