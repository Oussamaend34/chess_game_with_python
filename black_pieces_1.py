from pieces import *

class BlackPieces():
    def __init__(self, screen, settings,board):
        """initialize settings of the black pieces."""
        self.screen = screen
        self.settings = settings
        self.board = board
        # Make a king.
        self.king = King(screen, settings, board, x=4, y=0)
        # Make a queen.
        self.queen = Queen(screen, settings, board, x=3, y=0)
        self.Pawn_1 = Pawn(screen, settings, board, x=5, y=1)
        # the promoting pawn.
        self.promoting_pawn = None
        # Putting the black pieces in a list to easly manupilate them
        self.pieces = [
                        self.king, self.queen, self.Pawn_1
                      ]

    def pos(self):
        """Give black pieces there position on the screen"""
        for piece in self.pieces:
            piece.pos()
    def get_promoting(self):
        """create the promoting lists"""
        self.promoting_rect = []
        self.promoting_image = ["images/black_queen_promoting.png", "images/black_bishop_promoting.png", "images/black_knight_promoting.png", "images/black_rook_promoting.png"]
        for name in self.promoting_image:
            self.promoting_image[self.promoting_image.index(name)] = pygame.image.load(name)
        for i in range(4):
            self.promoting_rect.append(self.promoting_image[i].get_rect())
            self.promoting_rect[i].centery = 300
            self.promoting_rect[i].x = 10 + (i * 150)

    def promoting_blit(self):
        """blit the promoting list"""
        for i in range(4):
            self.screen.blit(self.promoting_image[i], self.promoting_rect[i])
    def promote(self, piece):
        """promote a pawn into one of the four pieces."""
        x=self.promoting_pawn.x
        y=self.promoting_pawn.y
        if piece == "Queen":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Queen(self.screen, self.settings, self.board, x=x, y=y, color="black"))
        elif piece == "Bishop":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Bishop(self.screen, self.settings, self.board, x=x, y=y, color="black"))
        elif piece == "Knight":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Knight(self.screen, self.settings, self.board, x=x, y=y, color="black"))
        elif piece == "Rook":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Rook(self.screen, self.settings, self.board, x=x, y=y, color="black"))
    def blitme(self):
        """draw piece on the screen."""
        for piece in self.pieces:
            piece.blitme()