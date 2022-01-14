# Implement your Model class here
import random
import view

class Model:
    def __init__(self, targets: int, projectile: int):
        self.targets = targets
        self.projectile = projectile
        self.balloons = []

    def return_projectile(self):
        return self.projectile

    def place_balloons(self):
        for i in range(self.return_projectile()):
            self.balloons.append((random.randint(0, 10), random.randint(0, 10)))


    def show_balloons(self):
        print(self.balloons)










