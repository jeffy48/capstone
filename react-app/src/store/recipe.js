const GET_RECIPES = "recipe/GET_RECIPES"

const get_recipes = (recipes) => ({
    type: GET_RECIPES,
    payload: recipes
})

export const get_recipes_thunk = () => async dispatch => {
    const res = await fetch('/api/recipes');
    try {
        const recipes = await res.json()
        dispatch(get_recipes(recipes))
    }
    catch(error) {
        return error
    }
}

const initialState = { all_recipes: [] }


export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_RECIPES:
            return {...state, all_recipes: action.payload}
		default:
			return state;
	}
}
