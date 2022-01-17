from view import View
from model import Model


class Controller:
    def __init__(self):
        self.model = Model(5,6)
        self.view = View(self)

    def main(self):
        self.view.main()


if __name__ == '__main__':
    calc = Controller()
    calc.model.initialize_positions()

    calc.main()