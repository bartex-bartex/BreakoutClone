import os
from Board import Board
import curses

class Game:
    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self, screen):
        y, x = screen.getmaxyx() # get terminal wymiary
        screen.resize(y, x)  # resize "virtual" terminal to original terminal

        board = Board(x, y - 1)  # leave space (when last cell is filled, cursor can't move anywhere)
        board.fill_boundaries(screen)
        screen.getch()