import random


class Model:
    def __init__(self, targets, projectiles):
        self.targets = targets
        self.projectiles = projectiles
        self.objects = []

        self.balloons = []

    def initialize_positions(self):
        self.launcher = (0,0)
        for i in range(self.projectiles):
            self.balloons.append((random.randint(1, 15), random.randint(0, 15)))

        self.objects.append(self.launcher)
        self.objects.append(self.balloons)

        return self.objects



