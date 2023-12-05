import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getGroceryListIngredientsThunk, updateGroceryListIngredientThunk } from "../../store/groceryList";

function GroceryListPage() {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const userId = user ? user.id : null
    const ingredients = useSelector(state => state.groceryList.groceryListIngredients)

    useEffect(() => {
        dispatch(getGroceryListIngredientsThunk(userId))
    }, [dispatch])

    const handleCheckBoxChange = (ingredientId, checked) => {
        const payload = {
            recipe_ingredient_id: ingredientId,
            user_id: userId,
            checked: checked
        }

        dispatch(updateGroceryListIngredientThunk(payload, ingredientId))
    }

    return (
        <div className="grocery-page">
            <div className="grocery-list">
                <h1>{user.username}'s Grocery List</h1>
                {ingredients.map(ingredient => (
                    <div>
                        <input type="checkbox" id={ingredient.id} name={ingredient.id} checked={ingredient.checked || false} onChange={(e) => handleCheckBoxChange(ingredient.id, e.target.checked)}/>
                        <label for={ingredient.id}>{ingredient.ingredient_quantity} {ingredient.ingredient_measurement} {ingredient.ingredient_name} {ingredient.ingredient_desc && (`(${ingredient.ingredient_desc})`)}</label>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default GroceryListPage;
