class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print("Bite")

    def strike(self):
        print("Strike")

    def slash(self):
        print("Slash")

    def kick(self):
        print("Kick")


monster1 = Monster(func=Attacks().bite)

monster1.func()
