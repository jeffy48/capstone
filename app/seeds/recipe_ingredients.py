from app.models import db, RecipeIngredient, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo recipe, you can add other recipes here if you want
def seed_recipe_ingredients():
    recipe_ingredient1 = RecipeIngredient(
        recipe_id=1,
        name="chicken",
        quantity=3,
        measurement="lbs",
        desc="whole"
    )
    recipe_ingredient2 = RecipeIngredient(
        recipe_id=1,
        name="salt",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient3 = RecipeIngredient(
        recipe_id=1,
        name="black pepper",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient4 = RecipeIngredient(
        recipe_id=1,
        name="onion powder",
        quantity=1,
        measurement="tbsp",
        desc="or to taste"
    )
    recipe_ingredient5 = RecipeIngredient(
        recipe_id=1,
        name="butter",
        quantity=0.5,
        measurement="cup",
        desc="or margarine"
    )
    recipe_ingredient6 = RecipeIngredient(
        recipe_id=1,
        name="celery",
        quantity=1,
        measurement="stalk",
        desc="leaves removed"
    )
    recipe_ingredient7 = RecipeIngredient(
        recipe_id=2,
        name="vegetable oil",
        quantity=3,
        measurement="tbsp"
    )
    recipe_ingredient8 = RecipeIngredient(
        recipe_id=2,
        name="beef stew meat",
        quantity=2,
        measurement="lbs",
        desc="cubed"
    )
    recipe_ingredient9 = RecipeIngredient(
        recipe_id=2,
        name="beef bouillon",
        quantity=4,
        measurement="cubes",
        desc="crumbled"
    )
    recipe_ingredient10 = RecipeIngredient(
        recipe_id=2,
        name="water",
        quantity=4,
        measurement="cups"
    )
    recipe_ingredient11 = RecipeIngredient(
        recipe_id=2,
        name="dried rosemary",
        quantity=1,
        measurement="tsp"
    )
    recipe_ingredient12 = RecipeIngredient(
        recipe_id=2,
        name="dried parsley",
        quantity=1,
        measurement="tsp"
    )
    recipe_ingredient13 = RecipeIngredient(
        recipe_id=2,
        name="black pepper",
        quantity=0.5,
        measurement="tsp"
    )
    recipe_ingredient14 = RecipeIngredient(
        recipe_id=2,
        name="large potatoes",
        quantity=3,
        measurement="whole",
        desc="peeled and cubed"
    )
    recipe_ingredient15 = RecipeIngredient(
        recipe_id=2,
        name="carrots",
        quantity=4,
        measurement="whole",
        desc="1 inch pieces"
    )
    recipe_ingredient16 = RecipeIngredient(
        recipe_id=2,
        name="celery",
        quantity=4,
        measurement="stalks",
        desc="1 inch pieces"
    )
    recipe_ingredient17 = RecipeIngredient(
        recipe_id=2,
        name="large onion",
        quantity=1,
        measurement="whole",
        desc="chopped"
    )
    recipe_ingredient18 = RecipeIngredient(
        recipe_id=2,
        name="cornstarch",
        quantity=2,
        measurement="tsp"
    )
    recipe_ingredient19 = RecipeIngredient(
        recipe_id=3,
        name="bacon",
        quantity=12,
        measurement="slices"
    )
    recipe_ingredient20 = RecipeIngredient(
        recipe_id=3,
        name="butter or margarine",
        quantity=0.66,
        measurement="cup"
    )
    recipe_ingredient21 = RecipeIngredient(
        recipe_id=3,
        name="all-purpose flour",
        quantity=0.66,
        measurement="cup"
    )
    recipe_ingredient22 = RecipeIngredient(
        recipe_id=3,
        name="milk",
        quantity=7,
        measurement="cups"
    )
    recipe_ingredient23 = RecipeIngredient(
        recipe_id=3,
        name="large potatoes",
        quantity=4,
        measurement="whole",
        desc="peeled and cubed"
    )
    recipe_ingredient24 = RecipeIngredient(
        recipe_id=3,
        name="green onions",
        quantity=4,
        measurement="stalks",
        desc="chopped"
    )
    recipe_ingredient25 = RecipeIngredient(
        recipe_id=3,
        name="cheddar cheese",
        quantity=1.25,
        measurement="cups",
        desc="shredded"
    )
    recipe_ingredient26 = RecipeIngredient(
        recipe_id=3,
        name="sour cream",
        quantity=1,
        measurement="cup"
    )
    recipe_ingredient27 = RecipeIngredient(
        recipe_id=3,
        name="salt",
        quantity=1,
        measurement="tsp"
    )
    recipe_ingredient28 = RecipeIngredient(
        recipe_id=3,
        name="ground black pepper",
        quantity=1,
        measurement="tsp"
    )
    recipe_ingredient29 = RecipeIngredient(
        recipe_id=4,
        name="beef fillet",
        quantity=2,
        measurement="400g",
        desc=""
    )
    recipe_ingredient30 = RecipeIngredient(
        recipe_id=4,
        name="olive oil",
        quantity=4,
        measurement="tbsp",
        desc="for frying"
    )
    recipe_ingredient31 = RecipeIngredient(
        recipe_id=4,
        name="wild mushrooms",
        quantity=500,
        measurement="g",
        desc="cleaned and chopped"
    )
    recipe_ingredient32 = RecipeIngredient(
        recipe_id=4,
        name="thyme",
        quantity=1,
        measurement="sprig",
        desc="leaves only"
    )
    recipe_ingredient33 = RecipeIngredient(
        recipe_id=4,
        name="puff pastry",
        quantity=500,
        measurement="g",
    )
    recipe_ingredient34 = RecipeIngredient(
        recipe_id=4,
        name="Parma ham",
        quantity=8,
        measurement="slices",
    )
    recipe_ingredient35 = RecipeIngredient(
        recipe_id=4,
        name="egg yolks",
        quantity=2,
        measurement="whole"
    )
    recipe_ingredient36 = RecipeIngredient(
        recipe_id=4,
        name="sea salt",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient37 = RecipeIngredient(
        recipe_id=4,
        name="black pepper",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient38 = RecipeIngredient(
        recipe_id=4,
        name="beef trimmings",
        quantity=200,
        measurement="g",
        desc="ask the butcher for these when trimming the fillet"
    )
    recipe_ingredient39 = RecipeIngredient(
        recipe_id=4,
        name="shallots",
        quantity=4,
        measurement="large",
        desc="peeled and sliced"
    )
    recipe_ingredient40 = RecipeIngredient(
        recipe_id=4,
        name="black peppercorns",
        quantity=12,
        measurement="whole"
    )
    recipe_ingredient41 = RecipeIngredient(
        recipe_id=4,
        name="bay leaf",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient42 = RecipeIngredient(
        recipe_id=4,
        name="red wine vinegar",
        quantity=1,
        measurement="splash"
    )
    recipe_ingredient43 = RecipeIngredient(
        recipe_id=4,
        name="red wine",
        quantity=1,
        measurement="750ml bottle"
    )
    recipe_ingredient44 = RecipeIngredient(
        recipe_id=4,
        name="beef stock",
        quantity=750,
        measurement="ml"
    )
    recipe_ingredient45 = RecipeIngredient(
        recipe_id=4,
        name="thyme sprig",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient46 = RecipeIngredient(
        recipe_id=5,
        name="ground beef",
        quantity=0.5,
        measurement="lb"
    )
    recipe_ingredient47 = RecipeIngredient(
        recipe_id=5,
        name="frozen chili",
        quantity=1,
        measurement="tsp",
        desc="grated"
    )
    recipe_ingredient48 = RecipeIngredient(
        recipe_id=5,
        name="bacon",
        quantity=3,
        measurement="strips"
    )
    recipe_ingredient49 = RecipeIngredient(
        recipe_id=5,
        name="onion",
        quantity=1,
        measurement="whole",
        desc="thickly sliced"
    )
    recipe_ingredient50 = RecipeIngredient(
        recipe_id=5,
        name="tomato",
        quantity=1,
        measurement="slice"
    )
    recipe_ingredient51 = RecipeIngredient(
        recipe_id=5,
        name="mayo",
        quantity=1,
        measurement="cup"
    )
    recipe_ingredient52 = RecipeIngredient(
        recipe_id=5,
        name="sriracha",
        quantity=2,
        measurement="tbsp",
        desc="or more to taste"
    )
    recipe_ingredient53 = RecipeIngredient(
        recipe_id=5,
        name="cheddar cheese",
        quantity=1,
        measurement="slice"
    )
    recipe_ingredient54 = RecipeIngredient(
        recipe_id=5,
        name="grapeseed oil",
        quantity=1,
        measurement="tbsp",
        desc="for frying"
    )
    recipe_ingredient55 = RecipeIngredient(
        recipe_id=5,
        name="butter",
        quantity=1,
        measurement="tbsp",
        desc="on bun"
    )
    recipe_ingredient56 = RecipeIngredient(
        recipe_id=6,
        name="chicken wings",
        quantity=2,
        measurement="lb",
        desc="lollipopped"
    )
    recipe_ingredient57 = RecipeIngredient(
        recipe_id=6,
        name="garlic powder",
        quantity=1,
        measurement="tbsp"
    )
    recipe_ingredient58 = RecipeIngredient(
        recipe_id=6,
        name="smoked paprika",
        quantity=1,
        measurement="tbsp"
    )
    recipe_ingredient59 = RecipeIngredient(
        recipe_id=6,
        name="kosher salt",
        quantity=1,
        measurement="tsp"
    )
    recipe_ingredient60 = RecipeIngredient(
        recipe_id=6,
        name="canola oil",
        quantity=2,
        measurement="tbsp"
    )
    recipe_ingredient61 = RecipeIngredient(
        recipe_id=6,
        name="unsalted butter",
        quantity=1,
        measurement="a few knobs"
    )
    recipe_ingredient62 = RecipeIngredient(
        recipe_id=6,
        name="black pepper",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient63 = RecipeIngredient(
        recipe_id=6,
        name="hot sauce",
        quantity=1,
        measurement="bottle",
        desc="of choice"
    )
    recipe_ingredient64 = RecipeIngredient(
        recipe_id=7,
        name="butter",
        quantity=1,
        measurement="tbsp"
    )
    recipe_ingredient65 = RecipeIngredient(
        recipe_id=7,
        name="chicken or turkey",
        quantity=1,
        measurement="whole",
        desc="small"
    )
    recipe_ingredient66 = RecipeIngredient(
        recipe_id=7,
        name="beef shank",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient67 = RecipeIngredient(
        recipe_id=7,
        name="marrow bones",
        quantity=2,
        measurement="up to 4"
    )
    recipe_ingredient68 = RecipeIngredient(
        recipe_id=7,
        name="onion",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient69 = RecipeIngredient(
        recipe_id=7,
        name="carrot",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient70 = RecipeIngredient(
        recipe_id=7,
        name="celery",
        quantity=2,
        measurement="stalks"
    )
    recipe_ingredient71 = RecipeIngredient(
        recipe_id=7,
        name="salt",
        quantity=1,
        measurement="touch"
    )
    recipe_ingredient72 = RecipeIngredient(
        recipe_id=7,
        name="Caputo '00' flour",
        quantity=454,
        measurement="grams"
    )
    recipe_ingredient73 = RecipeIngredient(
        recipe_id=7,
        name="whole eggs",
        quantity=258,
        measurement="grams",
        desc="beaten"
    )
    recipe_ingredient74 = RecipeIngredient(
        recipe_id=7,
        name="prosciutto di parma",
        quantity=12,
        measurement="oz"
    )
    recipe_ingredient75 = RecipeIngredient(
        recipe_id=7,
        name="imported mortadella",
        quantity=8,
        measurement="oz"
    )
    recipe_ingredient76 = RecipeIngredient(
        recipe_id=7,
        name="ground pork",
        quantity=8,
        measurement="oz"
    )
    recipe_ingredient77 = RecipeIngredient(
        recipe_id=7,
        name="egg",
        quantity=1,
        measurement="whole"
    )
    recipe_ingredient78 = RecipeIngredient(
        recipe_id=7,
        name="parmigiano reggiano",
        quantity=1,
        measurement="cup",
        desc="grated"
    )
    recipe_ingredient79 = RecipeIngredient(
        recipe_id=7,
        name="nutmeg",
        quantity=1,
        measurement="tsp",
        desc="grated"
    )
    recipe_ingredient80 = RecipeIngredient(
        recipe_id=7,
        name="white wine",
        quantity=0.5,
        measurement="cup"
    )
    recipe_ingredient81 = RecipeIngredient(
        recipe_id=7,
        name="unsalted butter",
        quantity=1,
        measurement="tbsp"
    )
    recipe_ingredient82 = RecipeIngredient(
        recipe_id=8,
        name="american cheese",
        quantity=110,
        measurement="grams"
    )
    recipe_ingredient83 = RecipeIngredient(
        recipe_id=8,
        name="cheddar cheese",
        quantity=110,
        measurement="grams",
        desc="good quality, slightly aged, or cheese of your choice"
    )
    recipe_ingredient84 = RecipeIngredient(
        recipe_id=8,
        name="whole milk",
        quantity=130,
        measurement="grams",
        desc="or 1/2 cup"
    )
    recipe_ingredient85 = RecipeIngredient(
        recipe_id=8,
        name="cavatelli",
        quantity=160,
        measurement="grams",
        desc="5-6 oz"
    )
    recipe_ingredient86 = RecipeIngredient(
        recipe_id=8,
        name="salt",
        quantity=1,
        measurement="to taste"
    )
    recipe_ingredient87 = RecipeIngredient(
        recipe_id=8,
        name="sodium citrate",
        quantity=0.25,
        measurement="tsp",
        desc="only if not using american cheese"
    )

    for i in range(1, 88):
        variable_name = f"recipe_ingredient{i}"
        recipe_ingredient = locals()[variable_name]
        db.session.add(recipe_ingredient)

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
