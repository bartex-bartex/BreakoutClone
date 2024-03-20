# Python way of creating static class is to simply declare methods without class
import math_helper

def display_center(text, row, screen, screen_width):
    """
    :param str text: Text to display
    :param int row: Display row, 1-based-index
    :param window screen: Curses screen on which to display
    :param int screen_width: The width of emulated screen
    """
    x = math_helper.calculate_center(screen_width, len(text))
    screen.addstr(row, x, text)