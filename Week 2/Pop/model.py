# Implement your Model class here
import builtins
import view
import controller


class Model(builtins.object):
    def __init__(self, targets, projectiles):
        self.targets = targets
        self.projectiles = projectiles

    def add_projectile(self, id, position):
        pass

    def advance_projectile(self, dx=.5, dy=0):
        pass

    def did_win(self):
        pass

    def get_launcher(self):
        pass

    def get_num_projectiles(self):
        pass

    def get_projectile_place(self):
        pass

    def get_status(self):
        pass

    def get_target_place(self):
        pass

    def get_targets(self):
        pass

    def handle_collisions(self):
        pass

    def game_over(self):
        pass

    def move_launcher(self, dx, dy=1):
        pass

    def shoot(self):
        pass

    def remove_projectile(self, position):
        pass

    def set_launcher(self, x, y):
        pass




