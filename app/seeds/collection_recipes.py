from app.models import db, CollectionRecipe, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a collection_recipe, you can add other collection_recipes here if you want
def seed_collection_recipes():
    collection_recipe1 = CollectionRecipe(
        collection_id=1,
        recipe_id=1
    )
    collection_recipe2 = CollectionRecipe(
        collection_id=1,
        recipe_id=2
    )
    collection_recipe3 = CollectionRecipe(
        collection_id=1,
        recipe_id=3
    )
    collection_recipe4 = CollectionRecipe(
        collection_id=2,
        recipe_id=1
    )
    collection_recipe5 = CollectionRecipe(
        collection_id=2,
        recipe_id=2
    )
    collection_recipe6 = CollectionRecipe(
        collection_id=2,
        recipe_id=3
    )
    collection_recipe7 = CollectionRecipe(
        collection_id=2,
        recipe_id=8
    )
    collection_recipe8 = CollectionRecipe(
        collection_id=3,
        recipe_id=4
    )
    collection_recipe9 = CollectionRecipe(
        collection_id=3,
        recipe_id=5
    )
    collection_recipe10 = CollectionRecipe(
        collection_id=3,
        recipe_id=6
    )
    collection_recipe11 = CollectionRecipe(
        collection_id=4,
        recipe_id=4
    )
    collection_recipe12 = CollectionRecipe(
        collection_id=4,
        recipe_id=5
    )
    collection_recipe13 = CollectionRecipe(
        collection_id=4,
        recipe_id=6
    )
    collection_recipe14 = CollectionRecipe(
        collection_id=4,
        recipe_id=8
    )
    collection_recipe15 = CollectionRecipe(
        collection_id=5,
        recipe_id=7
    )
    collection_recipe16 = CollectionRecipe(
        collection_id=5,
        recipe_id=8
    )
    collection_recipe17 = CollectionRecipe(
        collection_id=6,
        recipe_id=7
    )
    collection_recipe18 = CollectionRecipe(
        collection_id=6,
        recipe_id=8
    )
    collection_recipe19 = CollectionRecipe(
        collection_id=6,
        recipe_id=1
    )


    for i in range(1, 20):
        variable_name = f"collection_recipe{i}"
        collection_recipe = locals()[variable_name]
        db.session.add(collection_recipe)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_collection_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collection_recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collection_recipes"))

    db.session.commit()
