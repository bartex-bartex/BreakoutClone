class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
        # Create "2D" list
        # self.board = [[None for y in range(height)] for x in range(width)]
        
    def fill_boundaries(self, screen):
        screen.border('|', '|', '-', '-', '+', '+', '+', '+') 
        # screen.addstr(0, 0, '+')
        # for _ in range(0, self.width - 2):
        #     screen.addstr('-')
        # screen.addstr('+')

        # for i in range(0, self.height - 2):
        #     screen.addstr(i + 1, 0, '|')
        #     screen.addstr(i + 1, self.width - 1, '|')

        # screen.addstr(self.height - 1, 0, '+')
        # for _ in range(0, self.width - 2):
        #     screen.addstr('-')
        # screen.addstr('+')