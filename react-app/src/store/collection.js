const GET_USER_COLLECTIONS = "collection/GET_USER_COLLECTIONS";
const CREATE_COLLECTION = "collection/CREATE_COLLECTION";
const UPDATE_COLLECTION = "collection/UPDATE_COLLECTION";
const DELETE_COLLECTION = "collection/DELETE_COLLECTION";
const GET_ALL_COLLECTIONS = "collection/GET_ALL_COLLECTIONS";
const GET_COLLECTION = 'collection/GET_COLLECTION'

const getUserCollections = (collections) => ({
    type: GET_USER_COLLECTIONS,
    payload: collections
});

const createCollection = (collection) => ({
    type: CREATE_COLLECTION,
    payload: collection
});

const updateCollection = (collection) => ({
    type: UPDATE_COLLECTION,
    payload: collection
});

const deleteCollection = (collection) => ({
    type: DELETE_COLLECTION,
    payload: collection
})

const getAllCollections = (collections) => ({
    type: GET_ALL_COLLECTIONS,
    payload: collections
})

const getCollection = (collection) => ({
    type: GET_COLLECTION,
    payload: collection
})

// might have to rethink and change params
export const getUserCollectionsThunk = (userId) => async dispatch => {
    const res = await fetch(`/api/users/${userId}/collections`);
    try {
        const collections = await res.json()
        dispatch(getUserCollections(collections))
    }
    catch(error) {
        return error
    }
};

export const createCollectionThunk = (payload) => async dispatch => {
    const res = await fetch('/api/collections/', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    try {
        const collection = await res.json()
        dispatch(createCollection(collection))
        return collection
    }
    catch(error) {
        return error
    }
};

export const updateCollectionThunk = (collectionId, payload) => async dispatch => {
    const res = await fetch(`/api/collections/${collectionId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    try {
        const collection = await res.json()
        dispatch(updateCollection(collection))
        return collection;
    }
    catch(error) {
        return error
    }
};

export const deleteCollectionThunk = (collectionId) => async dispatch => {
    const res = await fetch(`/api/collections/${collectionId}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
    });
    try {
        const collection = await res.json()
        dispatch(deleteCollection(collection))
    }
    catch(error) {
        return error
    }
};

export const getAllCollectionsThunk = () => async dispatch => {
    const res = await fetch("/api/collections")
    try {
        const collections = await res.json()
        dispatch(getAllCollections(collections))
    }
    catch(error) {
        return error
    }
}

export const getCollectionThunk = (collectionId) => async dispatch => {
    const res = await fetch(`/api/collections/${collectionId}`)
    try {
        const collection = await res.json()
        dispatch(getCollection(collection))
    }
    catch(error) {
        return error
    }
}

const initialState = { collection: {}, collections: [], userCollections: [], collection: {}, createdCollection: {}, updatedCollection: {}, deletedCollection: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
        case GET_USER_COLLECTIONS:
            return {...state, userCollections: action.payload}
        case GET_COLLECTION:
            return {...state, collection: action.payload}
        case GET_ALL_COLLECTIONS:
            return {...state, collections: action.payload}
        case CREATE_COLLECTION:
            return {...state, createdCollection: action.payload}
        case UPDATE_COLLECTION:
            return {...state, collection: action.payload, updatedCollection: action.payload}
        case DELETE_COLLECTION:
            return {...state, deletedCollection: action.payload}
		default:
			return state;
	}
};
