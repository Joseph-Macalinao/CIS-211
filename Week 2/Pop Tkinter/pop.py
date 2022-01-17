import random
from tkinter import *
import model

root = Tk()



def main():
    mod = Model(4,6,root,0,0)
    mod.init_screen()
    mod.place_player()
    mod.check()


class Model:
    def __init__(self, arrows, targets, root, player_x, player_y):
        self.arrows = arrows
        self.targets = targets
        self.root = root
        self.player_x = player_x
        self.player_y = player_y

    def init_screen(self):
        for i in range(10):
            for e in range(10):
                lab = Label(self.root, text=' ')
                lab.grid(row=i, column=e)
        for i in range(self.targets):
            target = Label(self.root, text='🎈')
            target.grid(row=random.randint(0,9), column=random.randint(1,9))


    def place_player(self):
        player = Label(root, text='😃')
        player.grid(row=self.player_x, column=self.player_y)


    def move(self, direction):
        if direction.lower() == 'w':
            self.player_y += 1
            self.place_player()

    def check(self):
        inp = input()
        if inp.lower() == 'w' or inp.lower() == 's':
            self.move(inp)

root.mainloop()
main()
