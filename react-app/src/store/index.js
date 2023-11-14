import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import recipe from './recipe'
import recipeIngredient from './recipeIngredient'
import collection from './collection'
import collectionRecipe from './collectionRecipe'
import review from './review'
import groceryList from './groceryList'

const rootReducer = combineReducers({
  session,
  recipe,
  recipeIngredient,
  collection,
  collectionRecipe,
  review,
  groceryList
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
