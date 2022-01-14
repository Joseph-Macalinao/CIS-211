import builtins
import curses
from curses import wrapper
import controller
import model
# Implement your View class(es). I recommend using an abstract base class View,
# and inheriting the specific View for balloons and arrows from it, e.g., in
# a ViewBalloonPop class


class GameObject(builtins.object):
    def __init__(self, position, kind):
        self.position = position
        self.kind = kind

    def __str__(self):
        return f'Position: {self.position}\nKind: {self.kind}'

    def draw(self, screen: object=None):
        pass

    def get_position(self, position):
        return self.position

    def set_position(self, position):
        self.position = position


class View(builtins.object):
    def __init__(self):
        self.objects = []
        self.observers = []

    def add_input_observer(self, observer: object):
        self.observers.append(observer)

    def add_object(self, object: GameObject):
        self.objects.append(object)

    def game_over(self, won):
        pass

    def get_display_height(self):
        pass

    def get_display_width(self):
        pass

    def get_input(self):
        pass

    def get_projectile_name(self):
        pass

    def notify_input_observer(self, inputs: object):
        pass

    def remove_object(self, the_object: GameObject):
        pass

    def scale_x(self, x: float):
        pass

    def scale_y(self, y: float):
        pass

    def set_objects(self, objlist: list):
        pass

    def set_status(self, status):
        pass

    def targets_hit(self, targets: list):
        pass

    def update(self):
        pass



