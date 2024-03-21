from typing import List
from typing import Tuple
import helpers.math_helper as math_helper
from sprite import Sprite
from tile import Tile
from helpers.collision_checker import is_collision
from helpers.rectangle import Rectangle

class Ball:
    def __init__(self, sprite) -> None:
        self._calculate_start_position(sprite)
        self.move_vector = [-1, -1]

    def _calculate_start_position(self, sprite: Sprite):
        # Based ball position upon sprite position
        self.x = sprite.x + math_helper.calculate_center(sprite.length, 1)
        self.y = sprite.y - 1

    def update(self, sprite: Sprite, tiles: List[List[Tile]],  map_width, map_height, game) -> Tuple[bool, bool]:
        next_x, next_y = self.x + self.move_vector[0], self.y + self.move_vector[1]
        updated_tile = False

        if next_y == map_height - 1: # check for D boundary collision
            return False, False
        elif next_x == 0 or next_x == map_width - 1:  # check for L, R boundary collision
            self.move_vector = [self.move_vector[0] * -1, self.move_vector[1]]
        elif next_y == 0:  # check for U boundary collision 
            self.move_vector = [self.move_vector[0], self.move_vector[1] * -1]
        elif is_collision(next_x, next_y, Rectangle(sprite.x, sprite.y, sprite.length, 1)):  # check - sprite for collision
            self.move_vector = [self.move_vector[0], self.move_vector[1] * -1]
        else:
            for tile_row in tiles:
                for tile in tile_row:
                    if tile.is_broken == False and is_collision(next_x, next_y, tile.rect):
                        tile.is_broken = True
                        self.move_vector = [self.move_vector[0], self.move_vector[1] * -1]
                        game.score += 1
                        updated_tile = True

        self.x += self.move_vector[0]
        self.y += self.move_vector[1]

        return True, updated_tile