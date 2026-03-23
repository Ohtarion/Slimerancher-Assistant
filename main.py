'''This is a program that will be an assistant to the game 'Slimerancher 2'. It will be able to provide information about their different diets. '''

from flask import Flask, request, render_template_string


class Slime:
    def __init__(self, name, diet, favorite_food):
        self.name = name
        self.diet = diet
        self.favorite_food = favorite_food


class Main:
    def __init__(self):
        pass

    def get_diet(self, slime):
        return slime.diet

    def get_favorite_food(self, slime):
        return slime.favorite_food


PinkSlime = Slime("Pink Slime", "Everything", "No favorite food")
TabbySlime = Slime("Tabby Slime", "Meat", "Stony Hen")
PhosphorSlime = Slime("Phosphor Slime", "Veggies", "Cuberry")
RockSlime = Slime("Rock Slime", "Veggies", "Heart Beet")
BoomSlime = Slime("Boom Slime", "Meat", "Briar Hen")
HoneySlime = Slime("Honey Slime", "Veggies", "Mint Mango")
PuddleSlime = Slime("Puddle Slime", "Veggies", "Water")
CrystalSlime = Slime("Crystal Slime", "Veggies", "Odd Onion")
HuntSlime = Slime("Hunt Slime", "Meat", "Roostro")
FireSlime = Slime("Fire Slime", "Veggies", "Ashes")
LuckySlime = Slime("Lucky Slime", "Everything", "No favorite food")
GoldSlime = Slime("Gold Slime", "Everything", "Gilded Ginger")


app = Flask(__name__)

slimes = [PinkSlime, TabbySlime, PhosphorSlime, RockSlime, BoomSlime, HoneySlime, PuddleSlime, CrystalSlime, HuntSlime, FireSlime, LuckySlime, GoldSlime]


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
                background-color: #f0f0f0;
            }}
            h1 {{
                color: #333;
            }}
            select {{
                font-size: 18px;
                padding: 10px;
                margin: 20px 0;
            }}
            p {{
                font-size: 16px;
                color: #555;
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
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
