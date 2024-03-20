from curses import wrapper
from game import Game

def main():
    game = Game()
    wrapper(game.start)

if __name__ == '__main__':
    main()
