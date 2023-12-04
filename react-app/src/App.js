import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import AllRecipesPage from "./components/Recipes/AllRecipesPage";
import UserRecipesPage from "./components/MyRecipesPage";
import RecipePage from "./components/RecipePage";
import CreateRecipePage from "./components/CreateRecipePage";
import HomePage from "./components/HomePage";
import MyReviewsPage from "./components/MyReviewsPage";
import AllCollectionsPage from "./components/AllCollectionsPage";
import MyCollectionsPage from "./components/MyCollectionsPage";
import CreateCollectionPage from "./components/CreateCollectionPage";
import CollectionPage from "./components/CollectionPage";

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
