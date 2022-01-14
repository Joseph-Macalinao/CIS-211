import random
import os
from model import Model
from controller import Controller
class View:
    def __init__(self, x, y, arrows, balloons):
        self.x = x
        self.y = y
        self.arrows = arrows
        self.balloons = balloons
        self.display = []

    def init_screen(self):
        for i in range(self.y):
            row = []

            for e in range(self.x):
                row.append(" ")
            self.display.append(row)

    def place_objects(self):
        init_launch = random.randint(0, len(self.display)-1)
        self.display[init_launch][0] = '😃'

        for i in range(self.balloons):
            x_balloon_place = random.randint(1, len(self.display[0]))
            y_balloon_place = random.randint(0, len(self.display)-1)
            self.display[y_balloon_place][x_balloon_place] = '🎈'


    def show_screen(self):
        for i in self.display:
            print(i)

    def move(self):
        copy = self.display.copy()
        os.system('clear')
        while True:
            pass




v = View(10,10,2,3)
v.init_screen()
v.place_objects()
v.show_screen()
