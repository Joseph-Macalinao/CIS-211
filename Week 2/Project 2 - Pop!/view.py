import curses
from curses import wrapper
import controller
import model
# Implement your View class(es). I recommend using an abstract base class View,
# and inheriting the specific View for balloons and arrows from it, e.g., in
# a ViewBalloonPop class


class View:
    def __init__(self, screen, model):
        self.screen = screen
        self.model

    def inp(self):
        c1 = controller.Controller
        if curses.KEY_UP:
            controller.Controller.move(self.screen, 'up')


    def draw_player(self, x, y):
        self.screen.addstr(2, 2, '😃')



    def inp(self):
        c1 = controller.Controller(self.screen, )
        inputs = {curses.KEY_UP: 'up', curses.KEY_DOWN: 'down', 32: 'shoot'}
        controller.Controller.move()

    def main(self):
        curses.cbreak()
        curses.curs_set(0)  # Make cursor invisible

        # screen.keypad(True)
        self.screen.clear()
        self.screen.nodelay(True)

        dimensions = self.screen.getmaxyx()

        self.draw_player()


if __name__ == "__main__":
    # This will call main and pass it the curses window as the screen argument
    wrapper(View.main())

