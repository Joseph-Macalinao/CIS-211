from tkinter import *
import random


class Model:
    def __init__(self, arrows, targets, root):
        self.arrows = arrows
        self.targets = targets
        self.root = root

    def init_screen(self):
        for i in range(10):
            for e in range(10):
                lab = Label(self.root, text=' ')
                lab.grid(row=i, column=e)
        for i in range(self.targets):
            target = Label(self.root, text='🎈')
            target.grid(row=random.randint(0,9), column=random.randint(1,9))

        player = Label(self.root, text='😃')
        player.grid(row=0, column=0)

        return self.root