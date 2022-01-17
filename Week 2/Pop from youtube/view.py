import tkinter as tk
from tkinter import ttk




class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title(string='Pop')


    def mark(self, objects=[]):
        place = ''
        for i in objects:
            if i == 0:
                place +=  f'Launcher at: {str(objects[0])}\n'
            else:
                place += f'Ballon at: {str(objects[i])}\n'
        lab = tk.Label(text=place)
        lab.pack()



    def main(self):
        self.mark()
        self.mainloop()


