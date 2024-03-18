from Game import Game
from curses import wrapper

def main():
    game = Game()
    wrapper(game.start)

if __name__ == '__main__':
    main()
