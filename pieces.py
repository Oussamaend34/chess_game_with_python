import pygame
class Piece():
    """A class to store the settings of piece in genral"""
    def __init__(self, screen, settings, board, color = "black"):
        """Initialize pawn settings."""  
        self.screen = screen
        self.settings = settings
        self.board = board
        self.color = color
        if self.color == "black":
            self.piece_number = -1
        else:
            self.piece_number =  1
class Pawn(Piece):
    """A class to store pawn settings."""
    def __init__(self, screen, settings, board, x=5, y=6, color='black'):
        """Initialize pawn settings."""
        super().__init__(screen, settings, board, color)
        # load pawn image and get its rect.
        self.image_name = "images/" + self.color + "_pawn.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "Pawn"
    def __repr__(self):
        return "Pawn"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the pawn moves forward by one square except for the first time it can move for two squares.
        self.possible_moves = []
        if self.color == 'white':
            if self.y > 0:
                if self.settings.board[self.y - 1][self.x] == 0:
                    self.possible_moves.append([self.x, self.y - 1])
            if self.y == 6 and self.settings.board[self.y-1][self.x] == 0:
                if self.settings.board[self.y - 2][self.x] == 0:
                    self.possible_moves.append([self.x, self.y - 2])
            if self.y - 1 >= 0 and self.x -1 >= 0 and self.settings.board[self.y -1][self.x -1] == -self.piece_number:
                self.possible_moves.append([self.x - 1, self.y - 1])
            
            if self.y - 1 >= 0 and self.x +1 < 8 and self.settings.board[self.y -1][self.x +1] == -self.piece_number:
                self.possible_moves.append([self.x + 1,self.y - 1])
        if self.color == 'black':
            if self.y <= 6:
                if self.settings.board[self.y + 1][self.x] == 0:
                    self.possible_moves.append([self.x, self.y + 1])
            if self.y == 1 and self.settings.board[self.y+1][self.x] == 0:
                if self.settings.board[self.y + 2][self.x] == 0:
                    self.possible_moves.append([self.x, self.y + 2])
            if self.y + 1 <= 7 and self.x -1 >= 0 and self.settings.board[self.y +1][self.x -1] == -self.piece_number:
                self.possible_moves.append([self.x - 1, self.y + 1])
            
            if self.y + 1 < 8 and self.x + 1 < 8 and self.settings.board[self.y +1][self.x +1] == -self.piece_number:
                self.possible_moves.append([self.x + 1,self.y + 1])
    def pos(self):
        """Give pawn its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the pawn on the screen """
        self.screen.blit(self.image, self.rect)    
class Rook(Piece):
    """A class to store Rook settings."""
    def __init__(self, screen, settings, board, x= 0, y=0, color = 'black'):
        """Initialize rook settings."""
        super().__init__(screen, settings, board, color)
        # load rook image and get its rect.
        self.image_name = "images/" + self.color + "_rook.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "Rook"
    def __repr__(self):
        return "Rook"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the rook moves horizently and verticaly with any number of squares.
        self.possible_moves = []
        # First we check vertical moves.
        for pos in range(1,8):
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == -self.piece_number:
                self.possible_moves.append([self.x, self.y + pos])
                break
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == self.piece_number:
                break
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == 0:
                self.possible_moves.append([self.x, self.y + pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == -self.piece_number:
                self.possible_moves.append([self.x, self.y - pos])
                break
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == self.piece_number:
                break
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == 0:
                self.possible_moves.append([self.x, self.y - pos])
        # Second horizental moves.
        for pos in range(1,8):
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == -self.piece_number:
                self.possible_moves.append([self.x + pos, self.y])
                break
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == self.piece_number:
                break
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y])
        for pos in range(1,8):
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] == -self.piece_number:
                self.possible_moves.append([self.x - pos, self.y])
                break
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] == self.piece_number:
                break
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] != self.piece_number:
                self.possible_moves.append([self.x - pos, self.y])
        
    def pos(self):
        """Give rook its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the rook on the screen """
        self.screen.blit(self.image, self.rect)
class Bishop(Piece):
    """A class to store bishop settings."""
    def __init__(self, screen, settings, board, x=5,y=7, color = 'black'):
        """Initialize bishop settings."""
        super().__init__(screen, settings, board, color)
        # load pawn image and get its rect.
        self.image_name = "images/" + self.color + "_bishop.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "l3iba"
    def __repr__(self):
        return "l3iba"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the bishop moves diagnoly.
        self.possible_moves = []
        for pos in range(1,8):
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] == - self.piece_number:
                self.possible_moves.append([self.x + pos, self.y + pos])
                break
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] ==  self.piece_number: 
                break
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y + pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] == - self.piece_number:
                self.possible_moves.append([self.x + pos, self.y - pos])
                break
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] ==  self.piece_number: 
                break
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y - pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] == - self.piece_number:
                self.possible_moves.append([self.x - pos, self.y - pos])
                break
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] ==  self.piece_number: 
                break
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] == 0:
                self.possible_moves.append([self.x - pos, self.y - pos])
        for pos in range(1,8):
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] == - self.piece_number:
                self.possible_moves.append([self.x - pos, self.y + pos])
                break
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] ==  self.piece_number: 
                break
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] == 0:
                self.possible_moves.append([self.x - pos, self.y + pos])
        
    def pos(self):
        """Give bishop its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the bishop on the screen """
        self.screen.blit(self.image, self.rect)
class Queen(Piece):
    """A class to store queen settings."""
    def __init__(self, screen, settings, board, x=4,y=7, color = 'black'):
        """Initialize queen settings."""
        super().__init__(screen, settings, board, color)
        # load pawn image and get its rect.
        self.image_name = "images/" + self.color + "_queen.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "Queen"
    def __repr__(self):
        return "Queen"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the bishop moves diagnoly, horizently and verticaly.
        self.possible_moves = []
        # First we check vertical moves.
        for pos in range(1,8):
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == -self.piece_number:
                self.possible_moves.append([self.x, self.y + pos])
                break
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == self.piece_number:
                break
            if self.y + pos < 8 and self.settings.board[self.y + pos][self.x] == 0:
                self.possible_moves.append([self.x, self.y + pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == -self.piece_number:
                self.possible_moves.append([self.x, self.y - pos])
                break
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == self.piece_number:
                break
            if self.y - pos >= 0 and self.settings.board[self.y - pos][self.x] == 0:
                self.possible_moves.append([self.x, self.y - pos])
        # Second horizental moves.
        for pos in range(1,8):
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == -self.piece_number:
                self.possible_moves.append([self.x + pos, self.y])
                break
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == self.piece_number:
                break
            if self.x + pos < 8 and self.settings.board[self.y][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y])
        for pos in range(1,8):
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] == -self.piece_number:
                self.possible_moves.append([self.x - pos, self.y])
                break
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] == self.piece_number:
                break
            if self.x - pos >= 0 and self.settings.board[self.y][self.x - pos] != self.piece_number:
                self.possible_moves.append([self.x - pos, self.y])
        # Third diagonal moves.
        for pos in range(1,8):
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] == - self.piece_number:
                self.possible_moves.append([self.x + pos, self.y + pos])
                break
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] ==  self.piece_number: 
                break
            if self.y + pos < 8 and self.x + pos < 8 and self.settings.board[self.y + pos][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y + pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] == - self.piece_number:
                self.possible_moves.append([self.x + pos, self.y - pos])
                break
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] ==  self.piece_number: 
                break
            if self.y - pos >= 0 and self.x + pos < 8 and self.settings.board[self.y - pos][self.x + pos] == 0:
                self.possible_moves.append([self.x + pos, self.y - pos])
        for pos in range(1,8):
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] == - self.piece_number:
                self.possible_moves.append([self.x - pos, self.y - pos])
                break
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] ==  self.piece_number: 
                break
            if self.y - pos >= 0 and self.x - pos >= 0 and self.settings.board[self.y - pos][self.x - pos] == 0:
                self.possible_moves.append([self.x - pos, self.y - pos])
        for pos in range(1,8):
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] == - self.piece_number:
                self.possible_moves.append([self.x - pos, self.y + pos])
                break
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] ==  self.piece_number: 
                break
            if self.y + pos < 8 and self.x - pos >= 0 and self.settings.board[self.y + pos][self.x - pos] == 0:
                self.possible_moves.append([self.x - pos, self.y + pos])
        
    def pos(self):
        """Give queen its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the queen on the screen """
        self.screen.blit(self.image, self.rect)
class King(Piece):
    """A class to store king settings."""
    def __init__(self, screen, settings, board, x= 0, y=0, color = 'black'):
        """Initialize king settings."""
        super().__init__(screen, settings, board, color)
        # load pawn image and get its rect.
        self.image_name = "images/" + self.color + "_king.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "King"
    def __repr__(self):
        return "King"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the king moves by one square in any direction.
        self.possible_moves = []
        if self.y + 1 < 8 and self.settings.board[self.y + 1][self.x] != self.piece_number:
            self.possible_moves.append([self.x, self.y + 1])
        if self.y - 1 >= 0 and self.settings.board[self.y - 1][self.x] != self.piece_number:
            self.possible_moves.append([self.x, self.y - 1])
        if self.x + 1 < 8 and self.settings.board[self.y][self.x + 1] != self.piece_number:
            self.possible_moves.append([self.x + 1, self.y])
        if self.x - 1 >= 0 and self.settings.board[self.y][self.x - 1] != self.piece_number:
            self.possible_moves.append([self.x - 1, self.y])
        if self.y + 1 < 8 and self.x + 1 < 8 and self.settings.board[self.y + 1][self.x + 1] != self.piece_number:
                self.possible_moves.append([self.x + 1, self.y + 1])
        if self.y - 1 >= 0 and self.x + 1 < 8 and self.settings.board[self.y - 1][self.x + 1] != self.piece_number:
            self.possible_moves.append([self.x + 1, self.y - 1])
        if self.y - 1 >= 0 and self.x - 1 >= 0 and self.settings.board[self.y - 1][self.x - 1] != self.piece_number:
                self.possible_moves.append([self.x - 1, self.y - 1])
        if self.y + 1 < 8 and self.x - 1 >= 0 and self.settings.board[self.y + 1][self.x - 1] != self.piece_number:
            self.possible_moves.append([self.x - 1, self.y + 1])
    def pos(self):
        """Give king its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the king on the screen """
        self.screen.blit(self.image, self.rect) 
class Knight(Piece):
    """A class to store knight settings."""
    def __init__(self, screen, settings, board, x= 0, y=0, color = 'black'):
        """Initialize knight settings."""
        super().__init__(screen, settings, board, color)
        # load pawn image and get its rect.
        self.image_name = "images/" + self.color + "_knight.png"
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.possible_moves = []
        self.pos()
    def __str__(self):
        return "Knight"
    def __repr__(self):
        return "Knight"
    def poss_moves(self):
        """define the possible moves for the piece"""
        # the pawn moves forward by one square except for the first time it can move for two squares.
        self.possible_moves = []
        mark_1 = 1
        mark_2 = 1
        for index_1 in range(2):
            for index_2 in range(2):
                if self.x + mark_1 *2 in range(8) and self.y + mark_2 in range(8) and self.settings.board[self.y + mark_2][self.x + mark_1 *2] != self.piece_number:
                    self.possible_moves.append([self.x + mark_1 *2, self.y + mark_2])
                if self.x + mark_1 in range(8) and self.y + mark_2 *2 in range(8) and self.settings.board[self.y + mark_2 *2][self.x + mark_1] != self.piece_number:
                    self.possible_moves.append([self.x + mark_1, self.y + mark_2 *2])
                mark_2 *= -1
            mark_1 *= -1
        
    def pos(self):
        """Give pawn its position on the screen"""
        self.rect.center = self.board.board_rect[self.y][self.x].center

    def blitme(self):
        """draw the pawn on the screen """
        self.screen.blit(self.image, self.rect)
