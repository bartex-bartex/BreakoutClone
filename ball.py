from sprite import Sprite
import helpers.math_helper as math_helper

class Ball:
    def __init__(self, sprite) -> None:
        self.__calculate_start_position__(sprite)

    def __calculate_start_position__(self, sprite: Sprite):
        # Based ball position upon sprite position
        self.x = sprite.x + math_helper.calculate_center(sprite.length, 1)
        self.y = sprite.y - 1