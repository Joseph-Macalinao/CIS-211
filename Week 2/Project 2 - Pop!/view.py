import curses
import locale
from termios import VT1
import model
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
# Implement your View class(es). I recommend using an abstract base class View,
# and inheriting the specific View for balloons and arrows from it, e.g., in
# a ViewBalloonPop class


class View:
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size

    def return_x(self):
        return self.x_size

    def return_y(self):
        return self.y_size

    def screen(self):
        wind = curses.window()
        curses.cbreak()
        curses.curs_set(0)

        # screen.keypad(True)
        wind.clear()
        wind.nodelay(True)

    def draw_player(self, x, y):
        pass

    def main(self):
        v1 = View(15, 20)


if __name__ == "__main__":
    # This will call main and pass it the curses window as the screen argument
    curses.wrapper(View.main)


