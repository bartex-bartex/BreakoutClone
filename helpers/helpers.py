from helpers.rectangle import Rectangle

def is_collision(x, y, area: Rectangle) -> bool:
    return (area.x <= x <= area.x + area.width and
        area.y <= y <= area.y + area.height)

def display_center(text, row, screen, screen_width):
    """
    :param str text: Text to display
    :param int row: Display row, 1-based-index
    :param window screen: Curses screen on which to display
    :param int screen_width: The width of emulated screen
    """
    x = calculate_center(screen_width, len(text))
    screen.addstr(row, x, text)

def calculate_center(width, object_length = 1) -> int:
    """
    Calculate x position at which the text should begin.

    :param int width: Display screen width
    :param int object_length: How long is displayed object
    :return int: x position 
    """
    if object_length < 1:
        raise Exception('Width should be >= 1')

    if object_length == 1:
        return int((width - 1) // 2)
    else:
        return int((width + 1) // 2 - (object_length // 2))