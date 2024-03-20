from helpers.rectangle import Rectangle

def is_collision(x, y, area: Rectangle) -> bool:
    if (area.x <= x <= area.x + area.width and
        area.y <= y <= area.y + area.height):
        return True
    else:
        return False