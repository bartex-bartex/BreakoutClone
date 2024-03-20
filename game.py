import os
from board import Board
from sprite import Sprite
import curses

class Game:
    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self, screen):
        curses.curs_set(False)  # do not show cursor
        screen.nodelay(True)  # .getch() doesn't wait for key
        y, x = screen.getmaxyx() # get terminal wymiary
        screen.resize(y, x)  # resize "virtual" terminal to original terminal

        board = Board(x, y)
        sprite = Sprite(x, y)

        while True:
            board.draw_border(screen)
            board.draw_sprite(screen, sprite)

            key = screen.getch()

            if key == curses.KEY_RIGHT:
                sprite.move_right(board.width)
            elif key == curses.KEY_LEFT:
                sprite.move_left()
            elif key == ord('q'):
                break