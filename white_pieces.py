from pieces import *

class WhitePieces():
    def __init__(self, screen, settings,board):
        """initialize settings of the black pieces."""
        self.screen = screen
        self.settings = settings
        self.board = board
        # Make a king.
        self.king = King(screen, settings, board, x=4, y=7, color="white")
        # Make a queen.
        self.queen = Queen(screen, settings, board, x=3, y=7, color="white")
        # Make the bishops.
        self.bishop_1 = Bishop(screen, settings, board, x=2, y=7, color="white")
        self.bishop_2 = Bishop(screen, settings, board, x=5, y=7, color="white")
        # Make the knights.
        self.knight_1 = Knight(screen, settings, board, x=1, y=7, color="white")
        self.knight_2 = Knight(screen, settings, board, x=6, y=7, color="white")
        # Make the rooks.
        self.rook_1 = Rook(screen, settings, board, x=0, y=7, color="white")
        self.rook_2 = Rook(screen, settings, board, x=7, y=7, color="white")
        # Make the pawns.
        self.Pawn_1 = Pawn(screen, settings, board, x=0, y=6, color="white")
        self.Pawn_2 = Pawn(screen, settings, board, x=1, y=6, color="white")
        self.Pawn_3 = Pawn(screen, settings, board, x=2, y=6, color="white")
        self.Pawn_4 = Pawn(screen, settings, board, x=3, y=6, color="white")
        self.Pawn_5 = Pawn(screen, settings, board, x=4, y=6, color="white")
        self.Pawn_6 = Pawn(screen, settings, board, x=5, y=6, color="white")
        self.Pawn_7 = Pawn(screen, settings, board, x=6, y=6, color="white")
        self.Pawn_8 = Pawn(screen, settings, board, x=7, y=6, color="white")
        # the promoting pawn.
        self.promoting_pawn = None
        # Putting the black pieces in a list to easly manupilate them
        self.pieces = [
                        self.king, self.queen, self.bishop_1, self.bishop_2, self.knight_1, self.knight_2,
                        self.rook_1, self.rook_2, self.Pawn_1, self.Pawn_2, self.Pawn_3,
                        self.Pawn_4, self.Pawn_5, self.Pawn_6, self.Pawn_7, self.Pawn_8
                      ]

    def pos(self):
        """Give black pieces there position on the screen"""
        for piece in self.pieces:
            piece.pos()
    def get_promoting(self):
        """create the promoting lists"""
        self.promoting_rect = []
        self.promoting_image = ["images/white_queen_promoting.png", "images/white_bishop_promoting.png", "images/white_knight_promoting.png", "images/white_rook_promoting.png"]
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
            self.pieces.append(Queen(self.screen, self.settings, self.board, x=x, y=y, color="white"))
        elif piece == "Bishop":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Bishop(self.screen, self.settings, self.board, x=x, y=y, color="white"))
        elif piece == "Knight":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Knight(self.screen, self.settings, self.board, x=x, y=y, color="white"))
        elif piece == "Rook":
            self.pieces.remove(self.promoting_pawn)
            self.pieces.append(Rook(self.screen, self.settings, self.board, x=x, y=y, color="white"))
    def blitme(self):
        """draw piece on the screen."""
        for piece in self.pieces:
            piece.blitme()
    

