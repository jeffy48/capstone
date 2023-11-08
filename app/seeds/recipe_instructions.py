from app.models import db, RecipeInstruction, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_recipe_instructions():
    recipe_instruction1 = RecipeInstruction(
        recipe_id=1,
        desc="Preheat oven to 350 degrees F",
        instruction_num=1
    )
    recipe_instruction2 = RecipeInstruction(
        recipe_id=1,
        desc="Dry chicken skin with paper towel to get a nice, crispy skin",
        instruction_num=2
    )
    recipe_instruction3 = RecipeInstruction(
        recipe_id=1,
        desc="Season chicken inside and out. Place chicken on a roasting pan or a baking sheet and add butter to chicken and pan",
        instruction_num=3
    )
    recipe_instruction4 = RecipeInstruction(
        recipe_id=1,
        desc="Stuff the chicken cavity with celery and tuck wings under the body to prevent burning",
        instruction_num=4
    )
    recipe_instruction5 = RecipeInstruction(
        recipe_id=1,
        desc="Bake until chicken is fully roasted (about 1 hour 15 minutes)",
        instruction_num=5
    )
    recipe_instruction6 = RecipeInstruction(
        recipe_id=2,
        desc="Heat oil in a large pot or Dutch oven over medium-high heat; add beef and cook until well browned",
        instruction_num=1
    )
    recipe_instruction7 = RecipeInstruction(
        recipe_id=2,
        desc="Dissolve bouillon in 4 cups water and pour into the pot; stir in rosemary, parsley, and pepper. Bring to a boil; reduce heat to low, cover, and simmer for 1 hour. Stir in potatoes, carrots, celery, and onion.",
        instruction_num=2
    )
    recipe_instruction8 = RecipeInstruction(
        recipe_id=2,
        desc="Dissolve cornstarch in 2 teaspoons of cold water; stir into stew. Cover and simmer until beef is tender, about 1 hour.",
        instruction_num=3
    )
    recipe_instruction9 = RecipeInstruction(
        recipe_id=3,
        desc="Cook the bacon",
        instruction_num=1
    )
    recipe_instruction10 = RecipeInstruction(
        recipe_id=3,
        desc="Melt the butter, then whisk in the flour and milk.",
        instruction_num=2
    )
    recipe_instruction11 = RecipeInstruction(
        recipe_id=3,
        desc="Add the potatoes and onions and bring to a boil.",
        instruction_num=3
    )
    recipe_instruction12 = RecipeInstruction(
        recipe_id=3,
        desc="Reduce to a simmer, then stir in the remaining ingredients.",
        instruction_num=4
    )
    recipe_instruction13 = RecipeInstruction(
        recipe_id=3,
        desc="Cook until the cheese is melted.",
        instruction_num=5
    )
    recipe_instruction14 = RecipeInstruction(
        recipe_id=4,
        desc="Wrap each piece of beef tightly in a triple layer of cling film to set its shape, then chill overnight.",
        instruction_num=1
    )
    recipe_instruction15 = RecipeInstruction(
        recipe_id=4,
        desc="Remove the cling film, then quickly sear the beef fillets in a hot pan with a little olive oil for 30-60 seconds until browned all over and rare in the middle. Remove from the pan and leave to cool.",
        instruction_num=2
    )
    recipe_instruction16 = RecipeInstruction(
        recipe_id=4,
        desc="Finely chop the mushrooms and fry in a hot pan with a little olive oil, the thyme leaves and some seasoning. When the mushrooms begin to release their juices, continue to cook over a high heat for about 10 minutes until all the excess moisture has evaporated and you are left with a mushroom paste (known as a duxelle). Remove the duxelle from the pan and leave to cool.",
        instruction_num=3
    )
    recipe_instruction17 = RecipeInstruction(
        recipe_id=4,
        desc="Cut the pastry in half, place on a lightly floured surface and roll each piece into a rectangle large enough to envelop one of the beef fillets. Chill in the refrigerator.",
        instruction_num=4
    )
    recipe_instruction18 = RecipeInstruction(
        recipe_id=4,
        desc="Lay a large sheet of cling film on a work surface and place 4 slices of Parma ham in the middle, overlapping them slightly, to create a square. Spread half the duxelle evenly over the ham.",
        instruction_num=5
    )
    recipe_instruction19 = RecipeInstruction(
        recipe_id=4,
        desc="Season the beef fillets, then place them on top of the mushroom-covered ham. Using the cling film, roll the Parma ham over the beef, then roll and tie the cling film to get a nice, evenly thick log. Repeat this step with the other beef fillet, then chill for at least 30 minutes.",
        instruction_num=6
    )
    recipe_instruction20 = RecipeInstruction(
        recipe_id=4,
        desc="Brush the pastry with the egg wash. Remove the cling film from the beef, then wrap the pastry around each ham-wrapped fillet. Trim the pastry and brush all over with the egg wash. Cover with cling film and chill for at least 30 minutes.",
        instruction_num=7
    )
    recipe_instruction21 = RecipeInstruction(
        recipe_id=4,
        desc="Meanwhile, make the red wine sauce. Heat the oil in a large pan, then fry the beef trimmings for a few minutes until browned on all sides. Stir in the shallots with the peppercorns, bay and thyme and continue to cook for about 5 minutes, stirring frequently, until the shallots turn golden brown.",
        instruction_num=8
    )
    recipe_instruction22 = RecipeInstruction(
        recipe_id=4,
        desc="Pour in the vinegar and let it bubble for a few minutes until almost dry. Now add the wine and boil until almost completely reduced. Add the stock and bring to the boil again. Lower the heat and simmer gently for 1 hour, removing any scum from the surface of the sauce, until you have the desired consistency. Strain the liquid through a fine sieve lined with muslin. Check for seasoning and set aside.",
        instruction_num=9
    )
    recipe_instruction23 = RecipeInstruction(
        recipe_id=4,
        desc="When you are ready to cook the beef wellingtons, score the pastry lightly and brush with the egg wash again, then bake at 200°C/Gas 6 for 15-20 minutes until the pastry is golden brown and cooked. Rest for 10 minutes before carving.",
        instruction_num=10
    )
    recipe_instruction24 = RecipeInstruction(
        recipe_id=4,
        desc="Meanwhile, reheat the sauce. Serve the beef wellingtons sliced, with the sauce as an accompaniment.",
        instruction_num=11
    )
    recipe_instruction25 = RecipeInstruction(
        recipe_id=5,
        desc="Heat grill pan up medium high heat. Season beef mixture with salt and pepper, then add egg yolk and. grate frozen chili to taste (about 1 teaspoon on video) and mix together.",
        instruction_num=1
    )
    recipe_instruction26 = RecipeInstruction(
        recipe_id=5,
        desc="Coat grill pan with oil then form patty. if cooking in under 10 minutes, make your patty less than an inch, if you have time you can make bigger. Once formed put on grill pan (if cooking quickly, press it down slightly). Add bacon as well as onion which should seasoned with salt, pepper and oil.",
        instruction_num=2
    )
    recipe_instruction27 = RecipeInstruction(
        recipe_id=5,
        desc="Form Sriracha mayo by mixing components. Add more sriracha for personal taste",
        instruction_num=3
    )
    recipe_instruction28 = RecipeInstruction(
        recipe_id=5,
        desc="Flip onions and bacon once cooked on one side. Flip burger once seared and cooked through on one side (you will only flip once). Toast buns on grill pan for about 1-2 minutes",
        instruction_num=4
    )
    recipe_instruction29 = RecipeInstruction(
        recipe_id=5,
        desc="As your finishing cooking your burger, add slice of cheddar cheese to it. Add a little knob of butter and cover with bowl or pot to melt. Remove bacon and onions once cooked draining excess oil and fat.",
        instruction_num=5
    )
    recipe_instruction30 = RecipeInstruction(
        recipe_id=5,
        desc="Once cheese is melted and burger cooked, remove from heat and assemble: Bun, mayo, lettuce, tomato, onions, burger, bacon, onions, mayo and topped by the bun.",
        instruction_num=6
    )
    recipe_instruction31 = RecipeInstruction(
        recipe_id=6,
        desc="Preheat the oven to 375˚F (190˚C).",
        instruction_num=1
    )
    recipe_instruction32 = RecipeInstruction(
        recipe_id=6,
        desc="Pat chicken wings dry and add to a large bowl. Season the wings with garlic powder, smoked paprika and salt toss to combine.",
        instruction_num=2
    )
    recipe_instruction33 = RecipeInstruction(
        recipe_id=6,
        desc="Place a large oven-proof saute pan over medium-high heat and pour in the oil, letting it heat for a moment. Add the seasoned wings and butter to the pan and let crisp for a moment before turning the wings to crisp up the other side. Add black pepper and toss to coat evenly. Once most of the edges are crispy, and the butter is frothing, place the pan in the oven and bake for about 15 minutes, until golden, crispy and cooked through to 165˚F (73˚F).",
        instruction_num=3
    )
    recipe_instruction34 = RecipeInstruction(
        recipe_id=6,
        desc="Add wings to a large bowl, spoon on a few tablespoons of leftover pan sauce, a few splashes of hot sauce, a few knobs of butter, and toss, letting everything melt and form a glaze. Transfer to a clean dish to serve.",
        instruction_num=4
    )
    recipe_instruction35 = RecipeInstruction(
        recipe_id=7,
        desc="Place a 12 qt stock on the stove, place all the meat in the bottom of the pot, fill up with cold water and bring up to a gentle simmer. Wait to add the vegetables because as the broth comes up to a simmer, all of the impurities from the bones and meat will rise to the top and accumulate and when you don’t have a lot of stuff in the pot, it's easier to skim the “scum” out of the broth, which is the most important aspect of making a clear broth. It will take some time for the broth to get up to a simmer and while it does, every so often check on it, skim the scum and excess fat off the top and just begin the process of getting your stock nice and clean.",
        instruction_num=1
    )
    recipe_instruction36 = RecipeInstruction(
        recipe_id=7,
        desc="Once the broth is simmering, you’ll notice the scum accumulate faster, keep cleaning it, and once you notice it has slowed down somewhat, then gently add the rest of the aromatic vegetables. Bring it back up to a simmer. The main ingredients listed are my suggestions for a neutral stock. I want to use this for tortellini en Brodo so I don’t really want strong rosemary and thyme flavor but add it if you like.",
        instruction_num=2
    )
    recipe_instruction37 = RecipeInstruction(
        recipe_id=7,
        desc="Cook the broth for 12-24 hours, checking every so often to clean and scum or fat and to ensure the broth is simmering. We DO NOT want this to boil. Boiling will disturb the meat and cloudy the broth. I like to cook it for a minimum of 10 hours and up to 24. It takes around 24 hours to fully extract all the flavor out of the meat and bones.",
        instruction_num=3
    )
    recipe_instruction38 = RecipeInstruction(
        recipe_id=7,
        desc="After 12-24 hours, the broth should be golden and clear and slightly reduced. When it’s ready, let it cool for a bit so all the contents and impurities sink to the bottom of the pot, then it's time to strain. Using a ladle, gently dip it in the stock and pull out a ladle at a time to not disturb the stock and strain it through a fine mesh strainer into a big bowl. Then you could place it in the fridge to allow the fat to separate or you can add it to a fat separator and then strain it one more time through a cheesecloth into a quart container for storage to catch impurities in the stock. Then label them and store in the fridge for 3-4 days or the freezer for 6 months to a year.",
        instruction_num=4
    )
    recipe_instruction39 = RecipeInstruction(
        recipe_id=7,
        desc="Build a well of flour on the table and pour the beaten into the center. Using a fork, beat the egg like you're scrambling it while slowly incorporating the flour from the wall. Work it until the egg has the consistency of thick pancake batter. Then use a bench scraper and start to fold and cut in the flour until the mixture comes together and forms a ball. Then begin to knead the dough by hand. If it is sticky, add a tiny bit of flour at a time until it's no longer sticky but be careful not to add too much to make the dough dry. If the dough feels hard to knead, it’s probably too dry. Knead for 5-10 minutes, folding and rolling the dough onto itself and folding layers and air into the dough. Once the surface is soft and smoother, wrap it in plastic wrap and let it rest for 20-30 minutes to continue to hydrate and soften. After resting, knead the dough again for about 5 more minutes, it should be softer and much easier to knead. Then cut the dough in half, knead and shape each of the smaller balls into a nice round tight ball that is sealed and then wrap each piece in plastic and if you want to use it that day, let it rest at room temp until you’re ready to use, otherwise, for best results, rest in the fridge overnight. (Note: be sure to pull the dough out about 1 hour before you want to make pasta)",
        instruction_num=5
    )
    recipe_instruction40 = RecipeInstruction(
        recipe_id=7,
        desc="In a sauté pan on high heat, add a tablespoon of butter to the pan and cook it until it becomes brown butter. It will start spitting moisture and changing color and once the spitting stops and the butter is a nice golden brown with a nutty aroma, add the pork, season with salt and pepper and break it up with a flat bottomed wooden spoon to create smaller pieces which will allow more surface area to brown. Once the pork is browned all over and the pan is caramelizing and developing fond on the bottom of the pan, then deglaze with white wine and reduce until the pan is clean and there’s just a little liquid left over, then transfer it to a bowl to cool.",
        instruction_num=6
    )
    recipe_instruction41 = RecipeInstruction(
        recipe_id=7,
        desc="In a food processor, add the mortadella and prosciutto and process until it becomes a smooth mixture where the fat almost emulsifies the meats together. Now stop, scrap the sides of the bowl, then add the pork and continue processing for another 30 seconds to a minute. Then add in the egg, the cheese, the nutmeg and a little salt and pepper and then process until the mixture is a thick dough-like consistency. Then set aside until you’re ready to form the tortellini.",
        instruction_num=7
    )
    recipe_instruction42= RecipeInstruction(
        recipe_id=7,
        desc="You can use a pasta machine to roll the dough. Roll it out to the 7th or 8th setting of the pasta machine. However, today we will be practicing the art of pasta Fatto a Mano, or pasta made by hand and to do this we must use a Matarello, a specially designed long, perfectly straight rolling pin designed to roll out large singular sheets of circular pasta.",
        instruction_num=8
    )
    recipe_instruction43 = RecipeInstruction(
        recipe_id=7,
        desc="Take one of the balls of dough and take it in your hands and flatten it almost like you would a pizza dough. Now if the dough is very hydrated then you’ll need to dust it lightly with flour, but flour will also dry the dough out so if your dough is dryer, don’t add any flour. Then place it on the board with the mattarello, starting at the center for the dough with even pressure, roll away from you in one direction (12 o’clock), then rotate 90 degrees and repeat the process until the dough is too thin to rotate with your hand. Instead, starting on the far end of the dough, roll the dough towards you onto the mattarello then rotate the mattarello and unfurl the dough and begin to roll the do both straight ahead and at angles (11 o’clock, 12 o’clock and 1 o’clock) to ensure you maintain that circular shape. Then continue to roll the dough out until it’s thin enough to see through it or approximately the thickness of 4-5 post it notes.",
        instruction_num=9
    )
    recipe_instruction44 = RecipeInstruction(
        recipe_id=7,
        desc="Then cut the dough into 1 1/4 squares, a pasta bicycle will help this process. Then remove any pieces of dough that aren’t perfect squares then cover all the squares with plastic wrap to prevent them from drying out too quickly.",
        instruction_num=10
    )
    recipe_instruction45 = RecipeInstruction(
        recipe_id=7,
        desc="Then get out the filling or ripieno, take a handful at a time and expose only as many squares as you feel comfortable working with, pinch off about a small nut sized chunk of the filling and place it in the center of each square. Remember, the dough will dry out fast so the more squares you have exposed to the air, the faster you will need to work to prevent them from drying out. Then take a square and fold two of the points over the filling to meet to form a triangle. Now two points of dough just met, forming a double thickness dough. When you go to pinch the two points, pinch it hard enough to make the double thickness dough, back into a single thickness to match the rest of the thickness of the pasta. Then using your thumb and index finger, pinch down along the sides of the triangle, pushing out the air inside and then sealing the edges and again, making the double thickness dough into single thickness. Once you have a sealed triangle, hold one of the corners at the flat edge with your index finger and thumb and wrap it around your index finger until the two corners meet and then pinch them together to form a single thickness touch point. Then if they are dry enough you can place them right on the board, otherwise place on a tray with flour to prevent it from sticking. Don’t allow two tortellini to touch until they are dry enough to not stick. Repeat with the rest of the squares of dough.",
        instruction_num=11
    )
    recipe_instruction46 = RecipeInstruction(
        recipe_id=7,
        desc="In a high rimmed pot, add brodo and bring up to a bowl. The brodo is not seasoned yet so add enough salt until it tastes like a delish seasoned broth but not salty. There is no salt in the pasta either so we need to make sure the broth is seasoned enough for the broth to taste good and for the pasta to get seasoned. Once it’s seasoned and simmering, add the tortellini and cook for 3-5 minutes or until the pasta doesn’t taste raw at all.",
        instruction_num=12
    )
    recipe_instruction47 = RecipeInstruction(
        recipe_id=7,
        desc="The plate in a bowl with a touch of butter, make sure you get plenty of the small tortellini in the bowl and plenty of broth and finish with grated parmigiano reggiano. And you’re now ready to enjoy one of the most comforting dishes Italy has ever created.",
        instruction_num=13
    )
    recipe_instruction48 = RecipeInstruction(
        recipe_id=8,
        desc="First off, the one caveat to my 10 minute claim is your water must be boiling, and since we’re going to be using a double boiler technique, and this recipe is for 1, we’re going to use a smaller 4 quart sauce pot, and then a 3 quart saucier on top. The pasta cooks below, the sauce cooks gently up top. You could cook up to 2 servings with this size equipment. If you want to scale this recipe up which it is designed to do, you could use a bigger pot like a dutch oven maybe, with a large sautéed pan. Regardless, Get the water boiling ahead of time so its ready to go.",
        instruction_num=1
    )
    recipe_instruction49 = RecipeInstruction(
        recipe_id=8,
        desc="My preferred cheese blend is a 50/50 blend of American cheese and a slightly aged cheddar that I love. The American provides the creamy mouthfeel and also has the sodium citrate which is what gives it its distinct meltability. The cheddar brings big flavor. Again, if you didn’t want to use American, you could simply add sodium citrate to the milk and blend it together to melt and combine the sauce. But I’m using American cheese so I don’t have to do that. Personally, I think a little American cheese belongs in stove top Mac and cheese.",
        instruction_num=2
    )
    recipe_instruction50 = RecipeInstruction(
        recipe_id=8,
        desc="Shred and measure the cheese. Depending on the cheese you use, some have different moisture content, so I like to grate a little extra cheese just in case the sauce is a bit too thin, you can always add a bit more to adjust the thickness of the sauce later in the recipe. Then measure the milk and get it into the saucier that you’re going to make the sauce in.",
        instruction_num=3
    )
    recipe_instruction51 = RecipeInstruction(
        recipe_id=8,
        desc="Again for Mac and Cheese without American cheese, replace the American cheese with the real cheese of your choice, add 1/4 teaspoon of the sodium citrate and add to the milk before melting the cheese. If it appears slightly broken, Simply blend until emulsified. The sodium citrate is there to re-emulsify the fat and the protein in the cheese.",
        instruction_num=4
    )
    recipe_instruction52 = RecipeInstruction(
        recipe_id=8,
        desc="Now at the stove, with the water boiling in the sauce pot, add salt for the pasta and then place the saucier with the milk on top of the sauce pot, I’m going to set a stopwatch to show you how I’m going to get this done in under 10 minutes and let the milk warm up for a minute before introducing the cheese.",
        instruction_num=5
    )
    recipe_instruction53 = RecipeInstruction(
        recipe_id=8,
        desc="After a minute, get the pasta into the water, give it a stir, and then return the saucier to the sauce pot and begin to slowly add the cheese a few handfuls at a time, making sure the cheese is fully melted before adding another handful. If your heat is on high, make sure you lower it to a gentle simmer to make sure the water doesn’t boil over, and then keep working the cheese in until it's all completely dissolved.",
        instruction_num=6
    )
    recipe_instruction54 = RecipeInstruction(
        recipe_id=8,
        desc="The sauce should be nice and thick and creamy, just as promised. Now depending on what cheese you use, some have different moisture levels, you may need to just add a bit more cheese to get it to the right consistency, so if it feels thinner than this, add a bit more. The pasta should be al dente in about 6 minutes and once it's al dente, strain out the pasta and add it to the cheese sauce. If it's the right consistency, try to drain out as much of the pasta water as possible, or alternatively, if the sauce is too thick, a little pasta water will thin it out a bit. Then mix the sauce with the pasta until it coats each noodle, then turn off the heat, taste again and adjust the seasoning one last time, and we’re just at about 9 minutes and we’re ready to serve.",
        instruction_num=7
    )
    recipe_instruction55 = RecipeInstruction(
        recipe_id=8,
        desc="Get it into a bowl, but make sure the bowl isn’t cold or else the sauce will seize up fast. Warm it up in the microwave and then plate. The result is a thick and creamy Mac and cheese as promised with everything you love and want from that old box, but will have real flavor and be done in just about the same amount of time.",
        instruction_num=8
    )

    for i in range(1, 56):
        variable_name = f"recipe_instruction{i}"
        recipe_instruction = locals()[variable_name]
        db.session.add(recipe_instruction)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipe_instructions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipe_instructions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipe_instructions"))

    db.session.commit()
