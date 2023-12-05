const GET_ALL_RECIPES = "recipe/GET_ALL_RECIPES";
const GET_USER_RECIPES = "recipe/GET_USER_RECIPES";
const GET_RECIPE = "recipe/GET_RECIPE";
const CREATE_RECIPE = "recipe/CREATE_RECIPE";
const UPDATE_RECIPE = "recipe/UPDATE_RECIPE";
const DELETE_RECIPE = "recipe/DELETE_RECIPE";

const getAllRecipes = (recipes) => ({
    type: GET_ALL_RECIPES,
    payload: recipes
});

const getUserRecipes = (recipes) => ({
    type: GET_USER_RECIPES,
    payload: recipes
});

const getRecipe = (recipe) => ({
    type: GET_RECIPE,
    payload: recipe
});

const createRecipe = (recipe) => ({
    type: CREATE_RECIPE,
    payload: recipe
});

const updateRecipe = (recipe) => ({
    type: UPDATE_RECIPE,
    payload: recipe
});

const deleteRecipe = (recipe) => ({
    type: DELETE_RECIPE,
    payload: recipe
})

export const getAllRecipesThunk = () => async dispatch => {
    const res = await fetch('/api/recipes');
    try {
        const recipes = await res.json()
        dispatch(getAllRecipes(recipes))
    }
    catch(error) {
        return error
    }
};

// might have to rethink and change params
export const getUserRecipesThunk = (userId) => async dispatch => {
    const res = await fetch(`/api/users/${userId}/recipes`);
    try {
        const recipes = await res.json()
        dispatch(getUserRecipes(recipes))
    }
    catch(error) {
        return error
    }
};

export const getRecipeThunk = (recipeId) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipeId}`);
    try {
        const recipe = await res.json()
        dispatch(getRecipe(recipe))
    }
    catch(error) {
        return error
    }
};

export const createRecipeThunk = (payload) => async dispatch => {
    const res = await fetch('/api/recipes/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    try {
        const recipe = await res.json()
        console.log(recipe)
        dispatch(createRecipe(recipe))
        return recipe
    }
    catch(error) {
        console.log("hi", error)
        return error
    }
};

export const updateRecipeThunk = (recipeId, payload) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipeId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    try {
        const recipe = await res.json()
        dispatch(updateRecipe(recipe))
        return recipe
    }
    catch(error) {
        return error
    }
};

export const deleteRecipeThunk = (recipeId) => async dispatch => {
    const res = await fetch(`/api/recipes/${recipeId}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
    });
    try {
        const recipe = await res.json()
        dispatch(deleteRecipe(recipe))
    }
    catch(error) {
        return error
    }
};

const initialState = { allRecipes: [], userRecipes: [], recipe: {}, createdRecipe: {}, updatedRecipe: {}, deletedRecipe: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_ALL_RECIPES:
            return {...state, allRecipes: action.payload}
        case GET_USER_RECIPES:
            return {...state, userRecipes: action.payload}
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
