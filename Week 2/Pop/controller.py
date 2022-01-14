# Implement your Controller class here
import builtins
import model
import view


class Controller(builtins.object):
    def __init__(self, model: model.Model, view: view.View):
        self.model = model
        self.view = view

    def game_loop(self):
        pass

    def handle_user_input(self, action):
        pass

    def update_game_objects(self):
        pass



