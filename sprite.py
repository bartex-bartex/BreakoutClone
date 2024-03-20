from typing import Final
from directions_enum import Direction
import math_helper

INIT_LENGTH: Final[int] = 6  # initially Python doesn't have CONSTANTS, Final from 3.8

class Sprite:
    def __init__(self, map_width, map_height) -> None:
        self.length = INIT_LENGTH
        self.current_direction = None
        self.previous_direction = None
        self.x, self.y = self.__calculate_start_position__(map_width, map_height)

    def __calculate_start_position__(self, map_width, map_height):
        x = math_helper.calculate_center(map_width, self.length)
        y = map_height - 3

        return (x, y)

    def move_right(self, map_width):
        if self.x + self.length < map_width - 1:
            self.previous_direction = self.current_direction
            self.current_direction = Direction.RIGHT
            self.x += 1

    def move_left(self):
        if self.x != 1:
            self.previous_direction = self.current_direction
            self.current_direction = Direction.LEFT
            self.x -= 1
        