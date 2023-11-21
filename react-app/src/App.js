import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import AllRecipesPage from "./components/AllRecipesPage";
import UserRecipesPage from "./components/MyRecipesPage";
import RecipePage from "./components/RecipePage";

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
          <Route path="/my-recipes">
            <UserRecipesPage />
          </Route>
          <Route path="/recipes/:recipeId">
            <RecipePage />
          </Route>
          <Route path="/recipes">
            <AllRecipesPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
