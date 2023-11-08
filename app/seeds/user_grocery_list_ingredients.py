from app.models import db, UserGroceryListIngredient, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a user_grocery_list_ingredients, you can add other user_grocery_list_ingredients here if you want
def seed_user_grocery_list_ingredients():
    user_grocery_list_ingredient1 = UserGroceryListIngredient(
        user_id=1,
        recipe_ingredient_id=1,
        checked=False
    )
    user_grocery_list_ingredient2 = UserGroceryListIngredient(
        user_id=2,
        recipe_ingredient_id=7,
        checked=True
    )
    user_grocery_list_ingredient3 = UserGroceryListIngredient(
        user_id=2,
        recipe_ingredient_id=8,
        checked=False
    )
    user_grocery_list_ingredient4 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=82,
        checked=True
    )
    user_grocery_list_ingredient5 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=83,
        checked=True
    )
    user_grocery_list_ingredient6 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=84,
        checked=True
    )
    user_grocery_list_ingredient7 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=85,
        checked=True
    )
    user_grocery_list_ingredient8 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=86,
        checked=True
    )
    user_grocery_list_ingredient9 = UserGroceryListIngredient(
        user_id=3,
        recipe_ingredient_id=87,
        checked=True
    )

    for i in range(1, 10):
        variable_name = f"user_grocery_list_ingredient{i}"
        user_grocery_list_ingredient = locals()[variable_name]
        db.session.add(user_grocery_list_ingredient)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_grocery_list_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_grocery_list_ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_grocery_list_ingredients"))

    db.session.commit()
