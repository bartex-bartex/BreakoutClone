from time import sleep
from typing import Tuple
import curses
import helpers.helpers as helper
from board import Board
from sprite import Sprite
from ball import Ball
from tile import Tile
from helpers.rectangle import Rectangle

class Game:
    _WELCOME_MESSAGE = "Press SPACE to begin!"
    _FRAME_TIME = 1 / 10

    def __init__(self) -> None:
        self.score = 0

    def _arrange_tiles(self, rows_count, tile_width, tile_height, space_between_tiles, map_width, map_height, offset_from_left, offset_from_top):
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

    def _setup_curses(self, screen) -> Tuple[int, int]:
        curses.curs_set(False)  # do not show cursor
        y, x = screen.getmaxyx() # get terminal wymiary
        screen.resize(y, x)  # resize "virtual" terminal to original terminal
        return x, y
    
    def _initialize_game_objects(self, x, y):
        board = Board(x, y)
        sprite = Sprite(x, y)
        ball = Ball(sprite)
        self.tiles = self._arrange_tiles(3, 5, 1, 2, x, y, 3, 2)
        self.begin_tiles_count = self.get_tiles_amount_left()
        return board, sprite, ball

    def _draw_map(self, screen, board, ball, sprite, tiles = None, redraw_border = False):
        board.draw_ball(screen, ball)
        board.draw_sprite(screen, sprite)

        # In theory, border should be drawn only at the beginning
        if redraw_border == True:
            board.draw_border(screen)

        # None -> nothing to update
        if tiles != None:
            board.draw_tiles(tiles, screen)

    def _wait_for_user_start(self, screen, x, y):
        helper.display_center(self._WELCOME_MESSAGE, y - 2, screen, x)
        key = None
        while key != ord(' '):
            key = screen.getch()
        helper.display_center(' ' * len(self._WELCOME_MESSAGE), y - 2, screen, x)
        screen.nodelay(True)  # .getch() doesn't wait for key

    def _handle_user_input(self, screen, board, sprite):
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
            
    def _display_win_message(self, screen, x, y):
        helper.display_center('You win!', int(y / 2), screen, x)
        helper.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
        helper.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)

    def _display_lose_message(self, screen, x, y):
        helper.display_center('You lose...', int(y / 2), screen, x)
        helper.display_center(f'Your score is {self.score}', int(y / 2) + 1, screen, x)
        helper.display_center("Press 'q' to leave", int(y / 2) + 2, screen, x)

    def _wait_for_user_exit(self, screen):
        screen.nodelay(False)
        while True:
            key = screen.getch()
            if key == ord('q'):
                break

    def start(self, screen):
        x, y = self._setup_curses(screen)

        board, sprite, ball = self._initialize_game_objects(x, y)

        self._draw_map(screen, board, ball, sprite, self.tiles, True)

        self._wait_for_user_start(screen, x, y)

        update_tiles = False
        while True:
            if update_tiles == True:
                self._draw_map(screen, board, ball, sprite, self.tiles)
            else:
                self._draw_map(screen, board, ball, sprite)


            quit_game = self._handle_user_input(screen, board, sprite)
            if quit_game == True:
                break

            continue_game, update_tiles = ball.update(sprite, self.tiles, x, y, self)
            if continue_game == False:
                self._display_lose_message(screen, x, y)
                break
            elif self.begin_tiles_count == self.score:
                self._display_win_message(screen, x, y)
                break

            sleep(self._FRAME_TIME)
        
        self._wait_for_user_exit(screen)


