class Settings():
    """A class to store chess settings."""
    def __init__(self):
        """Initialize chess settings."""
        self.screen_width = 700
        self.square = self.screen_width / 8
        self.white_square = (240,240,240)
        self.black_square = (20, 20, 20)
        self.board = [
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [ 0,  0,  0,  0,  0,  0,  0,  0],
                      [ 0,  0,  0,  0,  0,  0,  0,  0],
                      [ 0,  0,  0,  0,  0,  0,  0,  0],
                      [ 0,  0,  0,  0,  0,  0,  0,  0],
                      [ 1,  1,  1,  1,  1,  1,  1,  1],
                      [ 1,  1,  1,  1,  1,  1,  1,  1]
                     ]
        # this settings set the turn 1 for white and -1 for black
        self.turn = 1
        # moving the pieces settings.
        self.clicked = False
        self.piece_move = None
        self.moved = False
        # check and checkmate and stalmate settings.
        self.black_check = False
        self.white_check = False
        self.checkmate = False
        self.stalemate = False
        # game stats settings.
        self.game_stats = True
        # promoting settings.
        self.promoting = False
        # white casteling settings.
        self.white_castling = True
        self.white_bishop_castling_poss = True
        self.white_bishop_castling = False
        self.white_queen_castling_poss = True
        self.white_queen_castling = False
        # black casteling settings.
        self.black_castling = True
        self.black_bishop_castling_poss = True
        self.black_bishop_castling = False
        self.black_queen_castling_poss = True
        self.black_queen_castling = False
        # en passant settings.
        self.en_passant_pawn_1= None
        self.en_passant_pawn_pos = None
        self.en_passant_pawn_2 = None
        self.black_en_passant = False
        self.white_en_passant = False