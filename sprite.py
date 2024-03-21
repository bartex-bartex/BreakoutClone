import helpers.helpers as helper
from enums.directions_enum import Direction

class Sprite:
    _DEFAULT_LENGTH = 6
    _DEFAULT_MOVEMENT_SPEED = 2

    def __init__(self, map_width, map_height) -> None:
        self.length = self._DEFAULT_LENGTH
        self.movement_speed = self._DEFAULT_MOVEMENT_SPEED
        self.current_direction = None
        self.x, self.y = self._calculate_start_position(map_width, map_height)

    def _calculate_start_position(self, map_width, map_height):
        x = helper.calculate_center(map_width, self.length)
        y = map_height - 3

        return (x, y)

    def move_right(self, map_width):
        if self.x + self.length < map_width - self.movement_speed:
            self.current_direction = Direction.RIGHT
            self.x += self.movement_speed

    def move_left(self):
        if self.x - 1 > self.movement_speed:
            self.current_direction = Direction.LEFT
            self.x -= self.movement_speed
        