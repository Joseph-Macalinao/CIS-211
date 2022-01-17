# Implement your Controller class here
import view

class Controller:
    def __init__(self, view1, model1):
        self.view = view1
        self.model = model1


    def game_loop(self):
        view.View.inp(self.view)


    def move(self, direction):
        if direction == 'up':
            print('yp')
        elif direction == 'down':
            pass
        elif direction == 32:
            pass