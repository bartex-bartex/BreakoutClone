import os
from board import Board
from sprite import Sprite
from ball import Ball
import helpers.display as display
import curses
from time import sleep

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
        ball = Ball(sprite)

        display.display_center("Press SPACE to begin!", 3, screen, x)

        while True:
            board.draw_border(screen)
            board.draw_sprite(screen, sprite)
            board.draw_ball(screen, ball)

            key = screen.getch()

            if key == curses.KEY_RIGHT:
                sprite.move_right(board.width)
            elif key == curses.KEY_LEFT:
                sprite.move_left()
            elif key == ord('q'):
                break

            continue_game = ball.update(sprite, x, y)
            
            # TODO - if tiles == 0 -> You win 
            if continue_game == False:
                display.display_center('You lose...', int(y / 2), screen, x)
                display.display_center('Your score is X', int(y / 2) + 1, screen, x)
                display.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)
                break

            sleep(0.1)
        
        screen.nodelay(False)
        while True:
            key = screen.getch()
            if key == ord('q'):
                break
