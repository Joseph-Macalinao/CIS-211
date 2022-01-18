#EVERYTHING RUNS FROM CONTROLLER, INITIALIZED IN CONTROLLER

from view import View
from model import Model


class Controller:
    def __init__(self):
        self.model = Model(5,8)
        self.view = View(self)
        self.view.add_input_observer(self)


    def handle_user_input(self, action: str):
        if action == 'up':
            calc.view.destroy()
            up = calc.model.move('up')
            calc.view.init_screen(up, calc.model.projectiles)
        elif action == 'down':
            calc.view.destroy()
            down = calc.model.move('down')
            calc.view.init_screen(down, calc.model.projectiles)
            calc.model.won()
        elif action == 'shoot':
            calc.view.destroy()
            shoot = calc.model.shoot()
            calc.view.init_screen(shoot, calc.model.projectiles)
            calc.model.won()
        win = calc.model.won()
        if win == True:
            calc.view.win(True)
        elif win == False:
            calc.view.win(False)

    def main(self):
        self.view.main()

    def aft(self):
        pushed = calc.view.pushed()
        if pushed == 'up':
            up = calc.model.move('up')
            calc.view.init_screen(up, calc.model.projectiles)
            calc.model.won()
        elif pushed == 'down':
            down = calc.model.move('down')
            calc.view.init_screen(down, calc.model.projectiles)
            calc.model.won()
        elif pushed == 'shoot':
            shoot = calc.model.shoot()
            calc.view.init_screen(shoot, calc.model.projectiles)
            calc.model.won()

        calc.view.after(1000, calc.aft)


if __name__ == '__main__':
    calc = Controller()
    places = calc.model.initialize_positions()
    calc.view.init_screen(places, calc.model.get_projectiles())
    calc.main()
