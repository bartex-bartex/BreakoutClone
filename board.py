import curses
from enums.colors_enum import Color
from enums.directions_enum import Direction

class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__prepare_colors__()

    def __prepare_colors__(self):
        curses.init_pair(Color.SPRITE.value, curses.COLOR_RED, curses.COLOR_WHITE)  # Sprite
        
    def draw_border(self, screen):
        screen.border('|', '|', '-', '-', '+', '+', '+', '+') 

    def draw_sprite(self, screen, sprite):
        screen.addstr(sprite.y, sprite.x, "█" * sprite.length, curses.color_pair(Color.SPRITE.value))
        # ■█□

        if sprite.current_direction == Direction.LEFT:
            # remove most right sprite cell
            screen.addstr(sprite.y, sprite.x + sprite.length, ' ' * sprite.movement_speed)
        elif sprite.current_direction == Direction.RIGHT:
            # remove most left sprite cell
            screen.addstr(sprite.y, sprite.x - sprite.movement_speed, ' ' * sprite.movement_speed)

    def draw_ball(self, screen, ball):
        screen.addstr(ball.y - ball.move_vector[1], ball.x - ball.move_vector[0], " ")
        screen.addstr(ball.y, ball.x, "o")