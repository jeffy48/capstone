const GET_RECIPE_INSTRUCTIONS = 'recipeInstruction/GET_RECIPE_INSTRUCTIONS';
const CREATE_RECIPE_INSTRUCTION = 'recipeInstruction/CREATE_RECIPE_INSTRUCTION';
const UPDATE_RECIPE_INSTRUCTION = 'recipeInstruction/UPDATE_RECIPE_INSTRUCTION';
const DELETE_RECIPE_INSTRUCTION = 'recipeInstruction/DELETE_RECIPE_INSTRUCTION';

const getRecipeInstructions = (instructions) => ({
	type: GET_RECIPE_INSTRUCTIONS,
	payload: instructions
});

const createRecipeInstruction = (instruction) => ({
	type: CREATE_RECIPE_INSTRUCTION,
	payload: instruction
});

const updateRecipeInstruction = (instruction) => ({
	type: UPDATE_RECIPE_INSTRUCTION,
	payload: instruction
});

const deleteRecipeInstruction = (instruction) => ({
	type: DELETE_RECIPE_INSTRUCTION,
	payload: instruction
})

export const getRecipeInstructionsThunk = (recipeId) => async dispatch => {
	const res = await fetch(`/api/recipes/${recipeId}/instructions`);
	try {
		const instructions = await res.json();
		dispatch(getRecipeInstructions(ingredients));
	}
	catch(error) {
		return error
	}
};

export const createRecipeInstructionThunk = (payload) => async dispatch => {
	const res = await fetch('/api/instructions', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
	try {
        const instruction = await res.json()
        dispatch(createRecipeInstruction(instruction))
    }
    catch(error) {
        return error
    }
};

export const updateRecipeInstructionThunk = (payload, id) => async dispatch => {
	const res = await fetch(`/api/instructions/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
	});
	try {
        const instruction = await res.json()
        dispatch(updateRecipeInstruction(instruction))
    }
    catch(error) {
        return error
    }
};

export const deletedRecipeInstructionThunk = (id) => async dispatch => {
	const res = await fetch(`/api/instructions/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
	});
	try {
        const instruction = await res.json()
        dispatch(deleteRecipeInstruction(instruction))
    }
    catch(error) {
        return error
    }
};

const initialState = { recipeInstructions: [], createdInstruction: {}, updatedInstruction: {}, deletedInstruction: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_RECIPE_INSTRUCTIONS:
            return {...state, recipeInstructions: action.payload}
		case CREATE_RECIPE_INSTRUCTION:
			return {...state, createdInstruction: action.payload}
		case UPDATE_RECIPE_INSTRUCTION:
			return {...state, updatedInstruction: action.payload}
		case DELETE_RECIPE_INSTRUCTION:
			return {...state, deletedInstruction: action.payload}
		default:
			return state;
	}
};
