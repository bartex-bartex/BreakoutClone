import os
from board import Board
from sprite import Sprite
from ball import Ball
from tile import Tile
import helpers.display as display
from helpers.rectangle import Rectangle
import curses
from time import sleep

class Game:
    def __init__(self) -> None:
        # os.system('cls' if os.name == 'nt' else 'clear')
        self.score = 0

    def arrange_tiles(self, rows_count, tile_width, tile_height, map_width, map_height, offset_from_top, offset_from_left):
        self.tiles = []
        
        n = int((map_width - 2) // 7)  # number of tiles in row
        for i in range(rows_count):
            i_row_tiles = []

            for j in range(n):
                tile_x = offset_from_left + j * (tile_width + 2)
                tile_y = offset_from_top + i * (tile_height + 1)
                
                if tile_y > map_height - 8:
                    break

                i_row_tiles.append(Tile(Rectangle(tile_x, tile_y, tile_width, tile_height), i))
            self.tiles.append(i_row_tiles)

    def get_tiles_left(self):
        not_broken = 0
        for tile_row in self.tiles:
            for tile in tile_row:
                if tile.is_broken == False:
                    not_broken += 1
        return not_broken

    def start(self, screen):
        curses.curs_set(False)  # do not show cursor
        y, x = screen.getmaxyx() # get terminal wymiary
        screen.resize(y, x)  # resize "virtual" terminal to original terminal

        board = Board(x, y)
        sprite = Sprite(x, y)
        ball = Ball(sprite)
        self.arrange_tiles(3, 5, 1, x, y, 3, 2)
        self.init_tiles_count = self.get_tiles_left()

        board.draw_border(screen)
        board.draw_sprite(screen, sprite)
        board.draw_ball(screen, ball)
        board.draw_tiles(self.tiles, screen)

        display.display_center("Press SPACE to begin!", 3, screen, x)
        key = None
        while key != ord(' '):
            key = screen.getch()
        screen.nodelay(True)  # .getch() doesn't wait for key

        while True:
            board.draw_border(screen)
            board.draw_sprite(screen, sprite)
            board.draw_ball(screen, ball)
            board.draw_tiles(self.tiles, screen)

            key = screen.getch()
            curses.flushinp()

            if key == curses.KEY_RIGHT:
                sprite.move_right(board.width)
            elif key == curses.KEY_LEFT:
                sprite.move_left()
            elif key == ord('q'):
                break

            continue_game = ball.update(sprite, self.tiles, x, y, self)
            
            if continue_game == False:
                display.display_center('You lose...', int(y / 2), screen, x)
                display.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
                display.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)
                break
            elif self.init_tiles_count == self.score:
                display.display_center('You win!', int(y / 2), screen, x)
                display.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
                display.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)

            sleep(1 / 10)
        
        screen.nodelay(False)
        while True:
            key = screen.getch()
            if key == ord('q'):
                break
