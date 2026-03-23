"""
Slime Rancher 2 Diet Assistant

This Flask web application serves as an interactive assistant for Slime Rancher 2 players.
It provides information about different slimes' diets and favorite foods.
The app runs on a local server and can be accessed via a web browser, making it
convenient for players using streaming setups like Moonlight/Sunshine.

Features:
- Dropdown selection of slimes
- Displays diet category and favorite food
- Dark mode UI for better gaming experience
- Mobile-responsive design
"""

from flask import Flask, request, render_template_string


class Slime:
    """
    Represents a slime in Slime Rancher 2.

    Attributes:
        name (str): The name of the slime (e.g., "Pink Slime").
        diet (str): The diet category (e.g., "Everything", "Meat", "Fruits", "Veggies").
        favorite_food (str): The slime's favorite food or "No favorite food".
    """

    def __init__(self, name, diet, favorite_food):
        self.name = name
        self.diet = diet
        self.favorite_food = favorite_food


class Food:
    """
    Represents a food item in Slime Rancher 2.

    Attributes:
        name (str): The name of the food (e.g., "Cuberry").
        type (str): The type of food (e.g., "Fruit", "Veggie", "Meat").
        eaten_by (list): A list of slimes that eat this food.
    """

    def __init__(self, name, type, eaten_by):
        self.name = name
        self.type = type
        self.eaten_by = eaten_by

    def get_type(self):
        """Returns the type of the food."""
        return self.type

    def get_eaten_by(self):
        """Returns a list of slimes that eat this food."""
        return self.eaten_by


class Main:
    """
    Main class for handling slime queries (currently not used in the web app,
    but kept for potential future CLI functionality).
    """

    def __init__(self):
        pass

    def get_diet(self, slime):
        """Returns the diet of the given slime."""
        return slime.diet

    def get_favorite_food(self, slime):
        """Returns the favorite food of the given slime."""
        return slime.favorite_food

    def show_image(self, slime):
        """Returns the image URL (in this case Honey_Slime.png in the images folder)"""
        return f"images/{slime.name.replace(' ', '_')}.png"


# Slime instantiations in alphabetical order
# These represent the slimes available in Slime Rancher 2 with their diets and favorites
AnglerSlime = Slime("Angler Slime", "Meat", "Sea Hen")
BattySlime = Slime("Batty Slime", "Fruit", "Pomegranite")
BoomSlime = Slime("Boom Slime", "Meat", "Briar Hen")
CottonSlime = Slime("Cotton Slime", "Veggies", "Water Lettuce")
CrystalSlime = Slime("Crystal Slime", "Veggies", "Odd Onion")
FireSlime = Slime("Fire Slime", "Veggies", "Ashes")
GoldSlime = Slime("Gold Slime", "Everything", "Gilded Ginger")
HoneySlime = Slime("Honey Slime", "Fruits", "Mint Mango")
HunterSlime = Slime("Hunt Slime", "Meat", "Roostro")
LuckySlime = Slime("Lucky Slime", "Everything", "No favorite food")
PhosphorSlime = Slime("Phosphor Slime", "Fruits", "Cuberry")
PinkSlime = Slime("Pink Slime", "Everything", "No favorite food")
PuddleSlime = Slime("Puddle Slime", "Veggies", "Water")
RockSlime = Slime("Rock Slime", "Veggies", "Heart Beet")
TabbySlime = Slime("Tabby Slime", "Meat", "Stony Hen")
TangleSlime = Slime("Tangle Slime", "Meat", "Painted Hen")
YolkySlime = Slime("Yolky Slime", "No diet", "No favorite food")
RingtailSlime = Slime("Ringtail Slime", "Fruits", "Pogo Fruit")

Briar_Hen = Food(
    "Briar Hen", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Carrot = Food(
    "Carrot", "Veggie",
    ["Pink Slime", "Rock Slime", "Cotton Slime", "Crystal Slime", "Ringtail Slime"]
)

Chickadoo = Food(
    "Chickadoo", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Cuberry = Food(
    "Cuberry", "Fruit",
    ["Pink Slime", "Phosphor Slime", "Honey Slime", "Batty Slime", "Ringtail Slime"]
)

Heart_Beet = Food(
    "Heart Beet", "Veggie",
    ["Pink Slime", "Rock Slime", "Cotton Slime", "Crystal Slime", "Ringtail Slime"]
)

Hen_Hen = Food(
    "Hen Hen", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Mint_Mango = Food(
    "Mint Mango", "Fruit",
    ["Pink Slime", "Phosphor Slime", "Honey Slime", "Batty Slime", "Ringtail Slime"]
)

Pogofruit = Food(
    "Pogo Fruit", "Fruit",
    ["Pink Slime", "Phosphor Slime", "Honey Slime", "Batty Slime", "Ringtail Slime"]
)

Roostro = Food(
    "Roostro", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Sea_Hen = Food(
    "Sea Hen", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Stony_Hen = Food(
    "Stony Hen", "Meat",
    ["Pink Slime", "Tabby Slime", "Boom Slime", "Hunter Slime",
        "Angler Slime", "Tangle Slime", "Ringtail Slime"]
)

Water_Lettuce = Food(
    "Water Lettuce", "Veggie",
    ["Pink Slime", "Rock Slime", "Cotton Slime", "Crystal Slime", "Ringtail Slime"]
)

Pomegranite = Food(
    "Pomegranite", "Fruit",
    ["Batty Slime", "Honey Slime", "Phosphor Slime", "Pink Slime", "Ringtail Slime"]
)

Ashes = Food(
    "Ashes", "Veggie",
    ["Fire Slime"]
)

Odd_Onion = Food(
    "Odd Onion", "Veggie",
    ["Crystal Slime", "Pink Slime", "Rock Slime", "Cotton Slime", "Ringtail Slime"]
)

Gilded_Ginger = Food(
    "Gilded Ginger", "Everything",
    ["Gold Slime", "Pink Slime", "Lucky Slime"]
)

Water = Food(
    "Water", "Veggie",
    ["Puddle Slime"]
)

Painted_Hen = Food(
    "Painted Hen", "Meat",
    ["Tangle Slime", "Pink Slime", "Tabby Slime", "Boom Slime",
        "Hunter Slime", "Angler Slime", "Ringtail Slime"]
)

slime_images = {
    "Pink Slime": "https://static.wikia.nocookie.net/slimerancher/images/e/e0/SlimePinkSR2.png",
    "Cotton Slime": "https://static.wikia.nocookie.net/slimerancher/images/3/3d/SlimeCottonSR2.png",
    "Tabby Slime": "https://static.wikia.nocookie.net/slimerancher/images/6/6e/SlimeTabbySR2.png",
    "Rock Slime": "https://static.wikia.nocookie.net/slimerancher/images/3/39/SlimeRockSR2.png",
    "Phosphor Slime": "https://static.wikia.nocookie.net/slimerancher/images/7/76/SlimePhosphorSR2.png",
    "Angler Slime": "https://static.wikia.nocookie.net/slimerancher/images/f/f9/SlimeAnglerSR2.png",
    "Batty Slime": "https://static.wikia.nocookie.net/slimerancher/images/0/0f/SlimeBattySR2.png",
    "Flutter Slime": "https://static.wikia.nocookie.net/slimerancher/images/5/5b/SlimeFlutterSR2.png",
    "Ringtail Slime": "https://static.wikia.nocookie.net/slimerancher/images/7/7f/SlimeRingtailSR2.png",
    "Honey Slime": "https://static.wikia.nocookie.net/slimerancher/images/8/8a/SlimeHoneySR2.png",
    "Hunter Slime": "https://static.wikia.nocookie.net/slimerancher/images/4/4c/SlimeHunterSR2.png",
    "Crystal Slime": "https://static.wikia.nocookie.net/slimerancher/images/e/e3/SlimeCrystalSR2.png",
    "Boom Slime": "https://static.wikia.nocookie.net/slimerancher/images/c/c1/SlimeBoomSR2.png",
    "Fire Slime": "https://static.wikia.nocookie.net/slimerancher/images/5/59/SlimeFireSR2.png",
    "Puddle Slime": "https://static.wikia.nocookie.net/slimerancher/images/2/2d/SlimePuddleSR2.png",
    "Yolky Slime": "https://static.wikia.nocookie.net/slimerancher/images/3/3a/SlimeYolkySR2.png",
    "Gold Slime": "https://static.wikia.nocookie.net/slimerancher/images/0/0c/SlimeGoldSR2.png",
    "Lucky Slime": "https://static.wikia.nocookie.net/slimerancher/images/2/2f/SlimeLuckySR2.png",
    "Dervish Slime": "https://static.wikia.nocookie.net/slimerancher/images/2/25/SlimeDervishSR2.png",
    "Tangle Slime": "https://static.wikia.nocookie.net/slimerancher/images/f/f1/SlimeTangleSR2.png",
    "Saber Slime": "https://static.wikia.nocookie.net/slimerancher/images/1/1e/SlimeSaberSR2.png",
    "Twin Slime": "https://static.wikia.nocookie.net/slimerancher/images/0/0d/SlimeTwinSR2.png",
    "Sloomber Slime": "https://static.wikia.nocookie.net/slimerancher/images/6/6a/SlimeSloomberSR2.png",
    "Hyper Slime": "https://static.wikia.nocookie.net/slimerancher/images/3/3c/SlimeHyperSR2.png",
    "Shadow Slime": "https://static.wikia.nocookie.net/slimerancher/images/5/5f/SlimeShadowSR2.png",

    # Special / states
    "Tarr": "https://static.wikia.nocookie.net/slimerancher/images/0/0e/SlimeTarrSR2.png"
}


app = Flask(__name__)

slimes = [AnglerSlime, BattySlime, BoomSlime, CottonSlime, CrystalSlime, FireSlime, GoldSlime, HoneySlime,
          HunterSlime, LuckySlime, PhosphorSlime, PinkSlime, PuddleSlime, RockSlime, TabbySlime, TangleSlime, YolkySlime, RingtailSlime]

food = [Briar_Hen, Carrot, Chickadoo, Cuberry, Heart_Beet, Hen_Hen,
        Mint_Mango, Pogofruit, Roostro, Sea_Hen, Stony_Hen, Water_Lettuce, Pomegranite, Ashes, Odd_Onion, Gilded_Ginger, Water, Painted_Hen]


@app.route('/', methods=['GET', 'POST'])
def home():
    selected_slime = request.form.get('slime')
    selected_food = request.form.get('food')

    slime_info = ""
    if selected_slime:
        slime = next((s for s in slimes if s.name == selected_slime), None)
        if slime:
            slime_info = f"Diet: {slime.diet}<br><br>Favorite Food: {slime.favorite_food}"
    food_info = ""
    if selected_food:
        food_item = next((f for f in food if f.name == selected_food), None)
        if food_item:
            food_info = f"Food type: {food_item.get_type()}<br><br>Eaten by: {', '.join(food_item.get_eaten_by())}"

    info = ""
    if slime_info and food_info:
        info = f"{slime_info}<br><br>{food_info}"
    elif slime_info:
        info = slime_info
    elif food_info:
        info = food_info

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Slime Rancher 2 Diet Assistant</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-image: url('/static/images/Slimerancher2_Background.png');
                background-size: cover;
                color: #ffffff;
            }}
            h1 {{
                color: #ffcc00;
            }}
            h2 {{
                color: #cccccc;
            }}
            .form-container {{
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin: 20px 0;
            }}
            .form-group {{
                text-align: center;
            }}
            .results {{
                display: flex;
                justify-content: space-around;
                margin: 20px 0;
            }}
            .result-box {{
                border: 1px solid #555555;
                padding: 10px;
                width: 45%;
                background-color: #222222;
                color: #cccccc;
            }}
            .images {{
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
            }}
            .images img {{
                max-width: 300px;
            }}
            p {{
                font-size: 16px;
                color: #cccccc;
            }}
        </style>
    </head>
    <body>
        <h1>Slime Rancher 2</h1>
        <br>
        <h2>Diet Assistant</h2>
        <div class="form-container">
            <div class="form-group">
                <label for="slime">Slime</label><br>
                <select name="slime" id="slime" onchange="this.form.submit()">
                    <option value="">Select a Slime</option>
                    {"".join(f'<option value="{s.name}"{" selected" if s.name == selected_slime else ""}>{s.name}</option>' for s in slimes)}
                </select>
            </div>
            <div class="form-group">
                <label for="food">Food</label><br>
                <select name="food" id="food" onchange="this.form.submit()">
                    <option value="">Select a Food</option>
                    {"".join(f'<option value="{f.name}"{" selected" if f.name == selected_food else ""}>{f.name}</option>' for f in food)}
                </select>
            </div>
        </div>
        <div class="results">
            <div class="result-box">
                <h3>Slime Info</h3>
                <p>{slime_info}</p>
            </div>
            <div class="result-box">
                <h3>Food Info</h3>
                <p>{food_info}</p>
            </div>
        </div>
        <div class="images">
            <img src="/static/images/{selected_slime.replace(' ', '')}.png" alt="{selected_slime}">
            <img src="/static/images/{selected_food.replace(' ', '')}.png" alt="{selected_food}">
        </div>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
