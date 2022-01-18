import random


class Model:
    def __init__(self, targets, projectiles):
        self.targets = targets
        self.projectiles = projectiles
        self.objects = []

    def get_targets(self):
        return self.targets

    def get_projectiles(self):
        return self.projectiles

    def get_objects(self):
        return self.objects

    def initialize_positions(self):
        self.launcher = (0,0)
        self.objects.append(self.launcher)
        for i in range(self.projectiles):
            self.objects.append((random.randint(1, 10), random.randint(0, 10)))
        return self.objects

    def move(self, deci):
        copy = self.objects.copy()
        if deci == 'up':
            copy[0] = (self.objects[0][0], self.objects[0][1] + 1)
        elif deci == 'down':
            copy[0] = (self.objects[0][0], self.objects[0][1] - 1)
        self.launcher = copy[0]
        self.objects[0] = copy[0]

        return self.objects

    def won(self):
        if self.projectiles == 0 and len(self.objects) != 1:
            return False
        elif self.projectiles >= 0 and len(self.objects) == 1:
            return True
        else:
            pass

    def shoot(self):
        for i in self.objects[1::]:
            if self.objects[0][1] == i[1]:
                self.objects.remove(i)
                self.targets -= 1
        if self.projectiles > 0:
            self.projectiles -= 1
        return self.objects





