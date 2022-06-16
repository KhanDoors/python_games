class Monster:
    def __init__(self, health, energy):
        print("Monster Created")
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("Monster Attacked")
        print(f"Monster Attacked {amount} times")
        self.health -= amount
        print(f"Monster health is now {self.health}")

    def move(self, speed):
        print("Monster Moved")
        print(f"Monster moved {speed} mph")
        self.health -= speed
        print(f"Monster health is now {self.health}")


class Shark(Monster):
    def __init__(self, health, energy, speed):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print("Shark Bit")


shark = Shark(speed=10, health=100, energy=50)
print(shark.attack(10))
