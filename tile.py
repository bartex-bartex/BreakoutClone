from helpers.rectangle import Rectangle

class Tile:
    def __init__(self, rect: Rectangle, row: int) -> None:
        self.rect = rect
        self.row = row
        self.is_broken = False