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
        nutrition (int): The nutritional value (not used in current implementation).
    """

    def __init__(self, name, type, nutrition):
        self.name = name
        self.type = type
        self.nutrition = nutrition


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

    def get_nutrition(self):
        """Returns the nutrition value of the food (placeholder)."""
        return self.nutrition

    def get_type(self):
        """Returns the type of the food."""
        return self.type

    def show_image(self, slime):
        """Returns a placeholder image URL for the slime (can be expanded)."""
        return "https://static.wikia.nocookie.net/slimerancher/images/e/e0/SlimePinkSR2.png/revision/latest?cb=20220922201720.png"


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


app = Flask(__name__)

slimes = [AnglerSlime, BattySlime, BoomSlime, CottonSlime, CrystalSlime, FireSlime, GoldSlime, HoneySlime,
          HunterSlime, LuckySlime, PhosphorSlime, PinkSlime, PuddleSlime, RockSlime, TabbySlime, TangleSlime, YolkySlime]


@app.route('/', methods=['GET', 'POST'])
def home():
    selected = request.form.get('slime')
    info = ""
    if selected:
        slime = next((s for s in slimes if s.name == selected), None)
        if slime:
            info = f"Diet: {slime.diet}<br>Favorite Food: {slime.favorite_food}"

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
                background-color: #121212;
                color: #ffffff;
            }}
            h1 {{
                color: #ffffff;
            }}
            select {{
                font-size: 18px;
                padding: 10px;
                margin: 20px 0;
                background-color: #333333;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 5px;
            }}
            p {{
                font-size: 16px;
                color: #cccccc;
            }}
        </style>
    </head>
    <body>
        <h1>Slime Rancher 2 Diet Assistant</h1>
        <form method="post">
            <select name="slime" onchange="this.form.submit()">
                <option value="">Select a Slime</option>
                {"".join(f'<option value="{s.name}">{s.name}</option>' for s in slimes)}
            </select>
        </form>
        <p>{info}</p>
        <img src="https://static.wikia.nocookie.net/slimerancher/images/e/e0/SlimePinkSR2.png/revision/latest?cb=20220922201720.png" alt="Pink Slime" width="200">
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
