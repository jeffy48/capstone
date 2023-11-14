const GET_GROCERY_LIST_INGREDIENTS = 'groceryList/GET_GROCERY_LIST_INGREDIENTS';
const CREATE_GROCERY_LIST_INGREDIENT = 'groceryList/CREATE_GROCERY_LIST_INGREDIENT';
const UPDATE_GROCERY_LIST_INGREDIENT = 'groceryList/UPDATE_GROCERY_LIST_INGREDIENT';
const DELETE_GROCERY_LIST_INGREDIENT = 'groceryList/DELETE_GROCERY_LIST_INGREDIENT';

const getGroceryListIngredients = (groceryListIngredients) => ({
	type: GET_GROCERY_LIST_INGREDIENTS,
	payload: groceryListIngredients
});

const createGroceryListIngredient = (groceryListIngredient) => ({
	type: CREATE_GROCERY_LIST_INGREDIENT,
	payload: groceryListIngredient
});

const updateGroceryListIngredient = (groceryListIngredient) => ({
	type: UPDATE_GROCERY_LIST_INGREDIENT,
	payload: groceryListIngredient
});

const deleteGroceryListIngredient = (groceryListIngredient) => ({
	type: DELETE_GROCERY_LIST_INGREDIENT,
	payload: groceryListIngredient
});

export const getGroceryListIngredientsThunk = (userId) => async dispatch => {
	const res = await fetch(`/api/users/${userId}/grocery-list-ingredients`);
	try {
		const groceryListIngredients = await res.json();
		dispatch(getGroceryListIngredients(groceryListIngredients));
	}
	catch(error) {
		return error
	}
};

export const createGroceryListIngredientThunk = (payload) => async dispatch => {
	const res = await fetch('/api/grocery-list-ingredients', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
	try {
        const groceryListIngredient = await res.json()
        dispatch(createGroceryListIngredient(groceryListIngredient))
    }
    catch(error) {
        return error
    }
};

export const updateGroceryListIngredientThunk = (payload, id) => async dispatch => {
	const res = await fetch(`/api/grocery-list-ingredients/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
	});
	try {
        const groceryListIngredient = await res.json()
        dispatch(updateGroceryListIngredient(groceryListIngredient))
    }
    catch(error) {
        return error
    }
};

export const deleteGroceryListIngredientThunk = (id) => async dispatch => {
	const res = await fetch(`/api/grocery-list-ingredients/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
	});
	try {
        const groceryListIngredient = await res.json()
        dispatch(deleteGroceryListIngredient(groceryListIngredient))
    }
    catch(error) {
        return error
    }
};

const initialState = { groceryListIngredients: [], createdListIngredient: {}, updatedListIngredient: {}, deletedListIngredient: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_GROCERY_LIST_INGREDIENTS:
            return {...state, groceryListIngredients: action.payload}
		case CREATE_GROCERY_LIST_INGREDIENT:
			return {...state, createdListIngredient: action.payload}
        case UPDATE_GROCERY_LIST_INGREDIENT:
            return {...state, updatedListIngredient: action.payload}
		case DELETE_GROCERY_LIST_INGREDIENT:
			return {...state, deletedListIngredient: action.payload}
		default:
			return state;
	}
};
