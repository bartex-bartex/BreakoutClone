from time import sleep
from typing import Tuple
import curses
import helpers.display as display
from board import Board
from sprite import Sprite
from ball import Ball
from tile import Tile
from helpers.rectangle import Rectangle

class Game:
    WELCOME_MESSAGE = "Press SPACE to begin!"  # constant variable
    FRAME_TIME = 1 / 10

    def __init__(self) -> None:
        self.score = 0

    def __arrange_tiles__(self, rows_count, tile_width, tile_height, space_between_tiles, map_width, map_height, offset_from_left, offset_from_top):
        tiles = []
        
        n = int((map_width - 2 - offset_from_left) / (tile_width + space_between_tiles))  # number of tiles in row
        for i in range(rows_count):
            ith_row_tiles = []

            for j in range(n):
                # tile upper-left corner coordination
                tile_x = 1 + offset_from_left + j * (tile_width + 2)
                tile_y = 1 + offset_from_top + i * (tile_height + 1)
                
                # leave some space between player and tiles
                if tile_y > map_height - 8:
                    break

                ith_row_tiles.append(Tile(Rectangle(tile_x, tile_y, tile_width, tile_height), i))
            tiles.append(ith_row_tiles)
        return tiles

    def get_tiles_amount_left(self) -> int:
        not_broken = 0
        for tile_row in self.tiles:
            for tile in tile_row:
                if tile.is_broken == False:
                    not_broken += 1
        return not_broken

    def __curses_setup__(self, screen) -> Tuple[int, int]:
        curses.curs_set(False)  # do not show cursor
        y, x = screen.getmaxyx() # get terminal wymiary
        screen.resize(y, x)  # resize "virtual" terminal to original terminal
        return x, y
    
    def __initialize_objects__(self, x, y):
        board = Board(x, y)
        sprite = Sprite(x, y)
        ball = Ball(sprite)
        self.tiles = self.__arrange_tiles__(3, 5, 1, 2, x, y, 3, 2)
        self.begin_tiles_count = self.get_tiles_amount_left()
        return board, sprite, ball

    def __draw_map__(self, screen, board, ball, sprite, tiles):
        board.draw_border(screen)
        board.draw_ball(screen, ball)
        board.draw_sprite(screen, sprite)
        board.draw_tiles(tiles, screen)

    def __welcome_user__(self, screen, x):
        display.display_center(self.WELCOME_MESSAGE, 3, screen, x)
        key = None
        while key != ord(' '):
            key = screen.getch()
        display.display_center(' ' * len(self.WELCOME_MESSAGE), 3, screen, x)
        screen.nodelay(True)  # .getch() doesn't wait for key

    def __handle_user_input__(self, screen, board, sprite):
            key = screen.getch()
            curses.flushinp()

            if key == curses.KEY_RIGHT:
                sprite.move_right(board.width)
                return False
            elif key == curses.KEY_LEFT:
                sprite.move_left()
                return False
            elif key == ord('q'):
                return True
            
    def __display_win_message__(self, screen, x, y):
        display.display_center('You win!', int(y / 2), screen, x)
        display.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
        display.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)

    def __display_lose_message__(self, screen, x, y):
        display.display_center('You lose...', int(y / 2), screen, x)
        display.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
        display.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)

    def __ask_for_leave__(self, screen):
        screen.nodelay(False)
        while True:
            key = screen.getch()
            if key == ord('q'):
                break

    def start(self, screen):
        x, y = self.__curses_setup__(screen)

        board, sprite, ball = self.__initialize_objects__(x, y)

        self.__draw_map__(screen, board, ball, sprite, self.tiles)

        self.__welcome_user__(screen, x)

        while True:
            self.__draw_map__(screen, board, ball, sprite, self.tiles)

            quit_game = self.__handle_user_input__(screen, board, sprite)
            if quit_game == True:
                break

            continue_game = ball.update(sprite, self.tiles, x, y, self)
            if continue_game == False:
                self.__display_lose_message__(screen, x, y)
                break
            elif self.begin_tiles_count == self.score:
                self.__display_win_message__(screen, x, y)
                break

            sleep(self.FRAME_TIME)
        
        self.__ask_for_leave__(screen)


