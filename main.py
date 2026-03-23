'''This is a program that will be an assistant to the game 'Slimerancher 2'. It will be able to provide information about their different diets. '''


class Slime:
    def __init__(self, name, diet):
        self.name = name
        self.diet = diet


class Main:
    def __init__(self):
        print("Hello, World!")

    def get_diet(self, slime):
        return slime.diet


PinkSlime = Slime("Pink Slime", "Omnivore")
RockSlime = Slime("Rock Slime", "Herbivore")

if __name__ == "__main__":
    main = Main()
    print(f"{PinkSlime.name} is an {main.get_diet(PinkSlime)}.")
    print(f"{RockSlime.name} is a {main.get_diet(RockSlime)}.")
