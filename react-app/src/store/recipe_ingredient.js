const GET_RECIPE_INGREDIENTS = 'recipe'


const initialState = { all_recipes: [], user_recipes: [], recipe: {}, createdRecipe: {}, updatedRecipe: {}, deletedRecipe: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_ALL_RECIPES:
            return {...state, all_recipes: action.payload}
		default:
			return state;
	}
};
