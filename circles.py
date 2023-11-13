import pygame
class GreenCircle():
    """A class for the circles that appears in the possible moves squares."""
    def __init__(self, screen, settings, board):
        """initialize the settings of the green circles."""
        self.screen = screen
        self.settings = settings
        self.piece = settings.piece_move
        self.board = board
        self.image = pygame.image.load("images/green_circle.png")
        self.rect = []

    def get_rect_circle(self):
        self.piece = self.settings.piece_move
        self.rect = []
        if self.piece != None:
            for move in self.piece.possible_moves:
                rect = self.image.get_rect()
                rect.center = self.board.board_rect[move[1]][move[0]].center
                self.rect.append(rect)
    
    def blitme(self):
        """draw the green circles on the screen."""
        for rect in self.rect:
            self.screen.blit(self.image, rect)


class RedCircle():
    """A class for the circles that appears if a king is in check or checkmate."""
    def __init__(self, screen, settings, board):
        """initialize the settings of the green circles."""
        self.screen = screen
        self.board = board
        self.image = pygame.image.load("images/red_circle.png")
        self.rect = self.image.get_rect()
    def get_pos(self, x_pos, y_pos):
        """get the pos of the king in danger"""
        self.rect.center = self.board.board_rect[y_pos][x_pos].center
    def blitme(self):
        """draw the green circles on the screen."""
        self.screen.blit(self.image, self.rect)