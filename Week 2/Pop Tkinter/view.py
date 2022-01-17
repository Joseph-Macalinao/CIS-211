from tkinter import *
import random
from model import Model

tk = Tk()
tk.mainloop()
class View:
    def __init__(self, screen, model):
        self.screen = screen
        self.model = model
        mod = model.Model

    def print_screen(self, screen):
        for i in range(10):
            for e in range(10):
                lab = Label(self.root, text=' ')
                lab.grid(row=i, column=e)
        for i in range(self.targets):
            target = Label(self.root, text='🎈')
            target.grid(row=random.randint(0,9), column=random.randint(1,9))

        player = Label(self.root, text='😃')
        player.grid(row=0, column=0)


