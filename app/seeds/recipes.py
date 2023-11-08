from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo recipe, you can add other recipes here if you want
def seed_recipes():
    recipe1 = Recipe(
        user_id=1,
        name='Juicy Roasted Chicken',
        servings=6,
        preptime=15,
        cooktime=75,
        difficulty='Easy',
        public=True,
        image='https://www.allrecipes.com/thmb/ZXXxFiCw2k7C-Uo_1UomrqAXrgM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/juicy-roasted-chicken-523131c0e0cf47319d8b87d3b3095f25.jpeg'
    )
    recipe2 = Recipe(
        user_id=1,
        name='Homemade Beef Stew',
        servings=10,
        preptime=20,
        cooktime=135,
        difficulty='Easy',
        public=True,
        image='https://www.allrecipes.com/thmb/KmVpU_AIw9ry-orvi4Ewz8DuAYM=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/25678-beef-stew-vi-humblepieliving-001-4x3-96b76b098c8642aea824065bce96df7e.jpg'
    )
    recipe3 = Recipe(
        user_id=1,
        name='Baked Potato Soup',
        servings=6,
        preptime=15,
        cooktime=25,
        difficulty='Easy',
        public=False,
        image='https://www.allrecipes.com/thmb/nEM9EwRCi53gaDkuHEPoF59pRnQ=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/baked-potato-soup-4x3-allrecipes-video-bf1bdf9a8578448c85683ad7eb0fbfe5.jpg'
    )
    recipe4 = Recipe(
        user_id=2,
        name="Gordan Ramsay's Beef Wellington",
        servings=4,
        preptime=105,
        cooktime=60,
        difficulty='Hard',
        public=True,
        image='https://www.gordonramsayrestaurants.com/assets/Uploads/_resampled/CroppedFocusedImage108081050-50-Classic-Gordon-Ramsay-Beef-Wellington.jpg'
    )
    recipe5 = Recipe(
        user_id=2,
        name="Gordan Ramsay's 10 Minute Burger" ,
        servings=1,
        preptime=5,
        cooktime=10,
        difficulty='Easy',
        public=True,
        image='https://i.ytimg.com/vi/ulhRORJpuBM/hq720.jpg?sqp=-oaymwEXCK4FEIIDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAh2GQJgir7vkE2jB_JOljMF_heZQ'
    )
    recipe6 = Recipe(
        user_id=2,
        name="Gordan Ramsay's Hot Ones Inspired Baked Chicken Wings",
        servings=4,
        preptime=15,
        cooktime=35,
        difficulty='Easy',
        public=False,
        image='https://www.gordonramsay.com/assets/Uploads/_resampled/CroppedFocusedImage108081050-50-BAKEDWINGS.jpg'
    )
    recipe7 = Recipe(
        user_id=3,
        name='Tortellini in Brodo',
        servings=4,
        preptime=60,
        cooktime=1440,
        difficulty='Medium',
        public=True,
        image='https://i.imgur.com/lwA6L8P.jpg'
    )
    recipe8 = Recipe(
        user_id=3,
        name='Stovetop Mac and Cheese',
        servings=4,
        preptime=10,
        cooktime=10,
        difficulty='Easy',
        public=True,
        image='https://i.imgur.com/odAXsqD.jpg'
    )

    for i in range(1, 9):
        print(recipe1)
        variable_name = f"recipe{i}"
        recipe = locals()[variable_name]
        db.session.add(recipe)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))

    db.session.commit()
