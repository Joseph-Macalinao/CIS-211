"""Main driver for a configuration with arrows shooting at balloon targets."""
import curses
from curses import wrapper

from view import ViewBalloonPop
from model import Model
from controller import Controller

def main(screen):
    view = ViewBalloonPop(screen)
    model = Model(5, 6)    # model with 5 targets and 6 projectiles
    controller = Controller(view, model)
    controller.game_loop()

if __name__ == "__main__":
    # This will call main and pass it the curses window as the screen argument
    wrapper(main)
