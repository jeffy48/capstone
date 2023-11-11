const GET_ALL_RECIPES = "recipe/GET_ALL_RECIPES";
const GET_USER_RECIPES = "recipe/GET_USER_RECIPES";
const GET_RECIPE = "recipe/GET_RECIPE";
const CREATE_RECIPE = "recipe/CREATE_RECIPE";
const UPDATE_RECIPE = "recipe/UPDATE_RECIPE";
const DELETE_RECIPE = "recipe/DELETE_RECIPE";

const get_all_recipes = (recipes) => ({
    type: GET_ALL_RECIPES,
    payload: recipes
});

const get_user_recipes = (recipes) => ({
    type: GET_USER_RECIPES,
    payload: recipes
});

const get_recipe = (recipe) => ({
    type: GET_RECIPE,
    payload: recipe
});

const create_recipe = (recipe) => ({
    type: CREATE_RECIPE,
    payload: recipe
});

const update_recipe = (recipe) => ({
    type: UPDATE_RECIPE,
    payload: recipe
});

const delete_recipe = (recipe) => ({
    type: DELETE_RECIPE,
    payload: recipe
})

export const get_all_recipes_thunk = () => async dispatch => {
    const res = await fetch('/api/recipes');
    try {
        const recipes = await res.json()
        dispatch(get_all_recipes(recipes))
    }
    catch(error) {
        return error
    }
};

// might have to rethink and change params
export const get_user_recipes_thunk = (user_id) => async dispatch => {
    const res = await fetch(`/api/users/${user_id}/recipes`);
    try {
        const recipes = await res.json()
        dispatch(get_user_recipes(recipes))
    }
    catch(error) {
        return error
    }
};

export const get_recipe_thunk = (recipe_id) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipe_id}`);
    try {
        const recipe = await res.json()
        dispatch(get_recipe(recipe))
    }
    catch(error) {
        return error
    }
};

export const create_recipe_thunk = (payload) => async dispatch => {
    const res = await fetch('/api/recipes', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    try {
        const recipe = await res.json()
        dispatch(create_recipe(recipe))
    }
    catch(error) {
        return error
    }
};

export const update_recipe_thunk = (recipe_id, payload) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipe_id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    try {
        const recipe = await res.json()
        dispatch(update_recipe(recipe))
    }
    catch(error) {
        return error
    }
};

export const delete_recipe_thunk = (recipe_id) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipe_id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
    });
    try {
        const recipe = await res.json()
        dispatch(delete_recipe(recipe))
    }
    catch(error) {
        return error
    }
};

const initialState = { all_recipes: [], user_recipes: [], recipe: {}, createdRecipe: {}, updatedRecipe: {}, deletedRecipe: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_ALL_RECIPES:
            return {...state, all_recipes: action.payload}
        case GET_USER_RECIPES:
            return {...state, user_recipes: action.payload}
        case GET_RECIPE:
            return {...state, recipe: action.payload}
        case CREATE_RECIPE:
            return {...state, createdRecipe: action.payload}
        case UPDATE_RECIPE:
            return {...state, updatedRecipe: action.payload}
        case DELETE_RECIPE:
            return {...state, deletedRecipe: action.payload}
		default:
			return state;
	}
};
