class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
        # Create "2D" list
        # self.board = [[None for y in range(height)] for x in range(width)]
        
    def draw_boundaries(self, screen):
        screen.border('|', '|', '-', '-', '+', '+', '+', '+') 