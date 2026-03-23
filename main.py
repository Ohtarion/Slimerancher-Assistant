'''This is a program that will be an assistant to the game 'Slimerancher 2'. It will be able to provide information about their different diets. '''


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


PinkSlime = Slime("Pink Slime", "Everything", "N/A")
TabbySlime = Slime("Tabby Slime", "Meat", "Stony Hen")
PhosphorSlime = Slime("Phosphor Slime", "Veggies", "Cuberry")
RockSlime = Slime("Rock Slime", "Veggies", "Heart Beet")
BoomSlime = Slime("Boom Slime", "Meat", "Briar Hen")
HoneySlime = Slime("Honey Slime", "Veggies", "Mint Mango")
PuddleSlime = Slime("Puddle Slime", "Veggies", "Water")
CrystalSlime = Slime("Crystal Slime", "Veggies", "Odd Onion")
HuntSlime = Slime("Hunt Slime", "Meat", "Roostro")
FireSlime = Slime("Fire Slime", "Veggies", "Ashes")
LuckySlime = Slime("Lucky Slime", "Everything", "N/A")
GoldSlime = Slime("Gold Slime", "Everything", "Gilded Ginger")


if __name__ == "__main__":
    main = Main()
    print(f"{PinkSlime.name} wants {main.get_diet(PinkSlime)} and likes to eat {main.get_favorite_food(PinkSlime)}.")
    print(f"{RockSlime.name} wants {main.get_diet(RockSlime)} and likes to eat {main.get_favorite_food(RockSlime)}.")
    print(f"{HuntSlime.name} wants {main.get_diet(HuntSlime)} and likes to eat {main.get_favorite_food(HuntSlime)}.")
