"""Main driver for a configuration with arrows shooting at balloon targets."""
import curses
from curses import wrapper

from view_text import View
from model_text import Model
from controller_text import Controller

def main():
    view = View()
    view.plan()