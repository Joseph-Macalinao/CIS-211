import tkinter as tk
from tkinter import ttk




class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title(string='Pop')


    def mark(self):
        lab = ttk.Label(text = f'')
        lab.pack()



    def main(self):
        self.mark()
        self.mainloop()


