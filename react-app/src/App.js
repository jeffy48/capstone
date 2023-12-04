import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/Auth/SignupFormPage";
import LoginFormPage from "./components/Auth/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation/Navigation";
import AllRecipesPage from "./components/Recipes/AllRecipiesPage";
import UserRecipesPage from "./components/Recipes/MyRecipePage";
import RecipePage from "./components/Recipes/RecipePage";
import CreateRecipePage from "./components/Recipes/CreateRecipePage";
import HomePage from "./components/HomePage/HomePage";
import MyReviewsPage from "./components/Reviews/MyReviewsPage";
import AllCollectionsPage from "./components/Collections/AllCollectionsPage";
import MyCollectionsPage from "./components/Collections/MyCollectionsPage";
import CreateCollectionPage from "./components/Collections/CreateCollectionPage";
import CollectionPage from "./components/Collections/CollectionPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/myreviews" >
            <MyReviewsPage />
          </Route>
          <Route path="/myrecipes">
            <UserRecipesPage />
          </Route>
          <Route path="/mycollections" >
            <MyCollectionsPage />
          </Route>
          <Route path="/recipes/create" >
            <CreateRecipePage />
          </Route>
          <Route path="/collections/create" >
            <CreateCollectionPage />
          </Route>
          <Route path="/recipes/:recipeId">
            <RecipePage />
          </Route>
          <Route path="/collections/:collectionId">
            <CollectionPage />
          </Route>
          <Route path="/recipes">
            <AllRecipesPage />
          </Route>
          <Route path="/collections" >
            <AllCollectionsPage />
          </Route>
          <Route path="/">
            <HomePage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
