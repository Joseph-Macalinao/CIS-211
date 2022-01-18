import tkinter as tk


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title(string='Pop')
        self.geometry('400x300+500+200')

        tk.Canvas(self, width=1000, height=750)
        self.observers = []

        # self.ent = tk.Entry(justify='right')
        # self.ent.insert(0,'w-up, d-down, space-shoot')
        # self.ent.grid(row=0, column=0)
    def add_input_observer(self, observer):
        self.observers.append(observer)

    def notify_input_observers(self, input: object):
        for observer in self.observers:
            observer.handle_user_input(input)


    def init_screen(self, objects=[1,2,3], projectiles=1):
        place = ''
        for i in sorted(objects):
            if i == objects[0]:
                place += f'Launcher at: {i}\n'
            else:
                place += f'Balloon at: {i}\n'

        project = tk.Label(text=f'Arrows left: {projectiles}')
        project.grid(row=1)
        lab = tk.Label(text=place, justify='center')
        lab.grid(row=2, column=0)
        #enter = tk.Button(text="Enter", command=self.get_ent)
        #enter.grid(row=1, column=1)
        up = tk.Button(text='Up', command=lambda: self.notify_input_observers('up'))
        up.grid(row=0, column=1)

        down = tk.Button(text='Down', command=lambda: self.notify_input_observers('down'))
        shoot = tk.Button(text='Shoot', command=lambda: self.notify_input_observers('shoot'))
        down.grid(row=0, column=2)
        shoot.grid(row=1,column=1)

    def pushed(self, deci=None):
        if deci == 'up':
            return 'up'  # just for debugging
        elif deci == 'down':
            return 'down'
        elif deci == 'shoot':
            return 'shoot'
        else:
            return None


    def pushed_down(self):
        return 'down'  # just for debugging

    def shoot(self):
        return 'shoot'

        #return 'shoot'
    def destroy(self):
        for child in self.winfo_children():
            child.destroy()


    def win(self, wl):
        if wl == True:
            self.init_screen([], 0)
            game_over = tk.Label(text='You won')
            game_over.grid(row=2, column=2)
        elif wl == False:
            self.init_screen([], 0)
            game_over = tk.Label(text='You lost')
            game_over.grid(row=2, column=2)


    def main(self):
        self.mainloop()



