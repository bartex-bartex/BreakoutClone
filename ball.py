from sprite import Sprite
import helpers.math_helper as math_helper
from helpers.collision_checker import is_collision
from helpers.rectangle import Rectangle

class Ball:
    def __init__(self, sprite) -> None:
        self.__calculate_start_position__(sprite)
        self.move_vector = [-1, -1]

    def __calculate_start_position__(self, sprite: Sprite):
        # Based ball position upon sprite position
        self.x = sprite.x + math_helper.calculate_center(sprite.length, 1)
        self.y = sprite.y - 1

    def update(self, sprite: Sprite, map_width, map_height) -> bool:
        next_x, next_y = self.x + self.move_vector[0], self.y + self.move_vector[1]

        if is_collision(next_x, next_y, Rectangle(sprite.x, sprite.y, sprite.length, 1)):  # check - sprite collision
            self.move_vector = [i * -1 for i in self.move_vector]
        elif next_y == map_height - 1: # check for D boundary collision
            return False
        elif next_x == 0 or next_x == map_width - 1:  # check for L, R boundary collision
            self.move_vector = [self.move_vector[0] * -1, self.move_vector[1]]
        elif next_y == 0:  # check for U boundary collision 
            self.move_vector = [self.move_vector[0], self.move_vector[1] * -1]

        self.x += self.move_vector[0]
        self.y += self.move_vector[1]

        return True