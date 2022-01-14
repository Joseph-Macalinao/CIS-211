def initialize_screen(x, y):
    screen = []
    for i in range(y):
        row = []
        for e in range(x):
            row.append(' ')
        screen.append(row)
        screen.append('\n')
    return screen

def print_screen(x, y):
    screen = initialize_screen(x, y)
    for i in screen:
        print(i)


def place_player(where, x, y):
    if y > len(initialize_screen(x, y)):
        where[(len(where)-1)][0] = '😃'
    where[y-1] = '😃'







def main():
    print_screen(5,4)


main()