import curses
import controller_text

class View:
    def plan(self):
        c1 = controller_text.Controller()
        do = input("What would you like to do:\nW - UP\nS - DOWN\nSPACEBAR - SHOOT")
        if do.upper() == 'W':
            controller_text.Controller.move(c1, 'up')
        elif do.upper() == 'D':
            controller_text.Controller.move(c1, 'down')
        elif do.upper() == ' ':
            controller_text.Controller.move(c1, 'shoot')