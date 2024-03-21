from typing import List
import curses
from enums.colors_enum import Color
from enums.directions_enum import Direction
from tile import Tile

class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self._prepare_colors()

    def _prepare_colors(self):
        curses.use_default_colors()  # Thanks to that -1 is transparent
        curses.init_pair(Color.SPRITE.value, curses.COLOR_RED, -1)  # Sprite
        curses.init_pair(Color.BALL.value, curses.COLOR_BLUE, -1)  # Ball
        curses.init_pair(Color.TILE.value, curses.COLOR_GREEN, -1)  # Tile
        
    def draw_border(self, screen):
        screen.border('|', '|', '-', '-', '+', '+', '+', '+') 

    def draw_sprite(self, screen, sprite):
        screen.addstr(sprite.y, sprite.x, "█" * sprite.length, curses.color_pair(Color.SPRITE.value))

        if sprite.current_direction == Direction.LEFT:
            # remove most right sprite cells
            screen.addstr(sprite.y, sprite.x + sprite.length, ' ' * sprite.movement_speed)
        elif sprite.current_direction == Direction.RIGHT:
            # remove most left sprite cells
            screen.addstr(sprite.y, sprite.x - sprite.movement_speed, ' ' * sprite.movement_speed)

    def draw_ball(self, screen, ball):
        screen.addstr(ball.y - ball.move_vector[1], ball.x - ball.move_vector[0], " ")
        screen.addstr(ball.y, ball.x, "⬤", curses.color_pair(Color.BALL.value))

    def draw_tiles(self, tiles: List[List[Tile]], screen: curses.window):
        for tile_row in tiles:
            for tile in tile_row:
                for i in range(tile.rect.height):
                    if tile.is_broken == False:
                        screen.addstr(tile.rect.y + i, tile.rect.x, "█" * tile.rect.width, curses.color_pair(Color.TILE.value))
                    else:
                        screen.addstr(tile.rect.y + i, tile.rect.x, " " * tile.rect.width)
                    
