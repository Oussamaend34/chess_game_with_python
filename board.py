import pygame 
class Board():
    """A class to store the board attributes"""
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.board_rect = []
        self.board = []
        self.create_board()
        self.get_rect_board()

    def create_board(self):
        """set the board to white and black"""
        mark = -1
        for row in range(8):
            mark *= -1
            temp_row = []
            for colomn in range(8):
                temp_row.append(mark)
                mark *= -1
            self.board.append(temp_row)

    def get_rect_board(self):
        """Make rectangles of evrey square on the board."""
        for row in range(8):
            temp_row = []
            for colomn in range(8):
                temp_row.append(pygame.Rect(colomn *self.settings.square, row * self.settings.square, self.settings.square, self.settings.square))  
            self.board_rect.append(temp_row)


    def draw_board(self):
        for row in range(8):
            for colomn in range(8):
                if self.board[row][colomn] == 1:
                    pygame.draw.rect(self.screen, self.settings.white_square,self.board_rect[row][colomn])
                if self.board[row][colomn] == -1:
                    pygame.draw.rect(self.screen, self.settings.black_square,self.board_rect[row][colomn])
