class Monster:
    def __init__(self, health, energy):
        print("Monster Created")
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __str__(self):
        return f"Monster health is {self.health}"

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


monster1 = Monster(10, 20)

print(monster1)
