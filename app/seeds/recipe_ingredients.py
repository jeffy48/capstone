from app.models import db, RecipeIngredient, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo recipe, you can add other recipes here if you want
def seed_recipe_ingredients():
    recipe_ingredient1 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient2 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient3 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient4 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient5 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient6 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient7 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient8 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient9 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=1,
        measurement="whole"
    )

    db.session.add(recipe_ingredient1)
    db.session.add(recipe_ingredient2)
    db.session.add(recipe_ingredient3)
    db.session.add(recipe_ingredient4)
    db.session.add(recipe_ingredient5)
    db.session.add(recipe_ingredient6)
    db.session.add(recipe_ingredient7)
    db.session.add(recipe_ingredient8)
    db.session.add(recipe_ingredient9)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipe_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipe_ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipe_ingredients"))

    db.session.commit()
