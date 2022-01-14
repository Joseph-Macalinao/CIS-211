# Implement your Model class here
import random
import view_text
import controller_text

class Model:
    def __init__(self, targets: int, projectile: int):
        self.targets = targets
        self.projectile = projectile
        self.balloons = []

    def return_projectile(self):
        return self.projectile

    def return_balloons(self):
        return list(self.balloons)

    def place_balloons(self):
        for i in range(self.return_projectile()):
            self.balloons.append((random.randint(0, 10), random.randint(0, 10)))

    def show_balloons(self):
        for i in self.return_balloons():
            print(f'Balloon at: {i}')


m1 = Model(5, 3)
m1.place_balloons()
m1.show_balloons()













