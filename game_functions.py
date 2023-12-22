import pygame
import sys

def check_events(settings, black_pieces,white_pieces, green_circle, red_circle):
    """Check events of the game."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and settings.clicked == False and settings.game_stats == False:
            x_pos, y_pos = pygame.mouse.get_pos()
            if settings.promoting == True:
                if settings.turn == -1:
                    for rect in black_pieces.promoting_rect:
                        if rect.collidepoint(x_pos, y_pos):
                            if black_pieces.promoting_rect.index(rect) == 0:
                                piece = "Queen"
                            if black_pieces.promoting_rect.index(rect) == 1:
                                piece = "Bishop"
                            if black_pieces.promoting_rect.index(rect) == 2:
                                piece = "Knight"
                            if black_pieces.promoting_rect.index(rect) == 3:
                                piece = "Rook"
                            settings.promoting = False
                            settings.game_stats = True
                            black_pieces.promote(piece)
                            settings.turn *= -1
                            check(settings, black_pieces, white_pieces, red_circle)
                            check_for_checkmate(settings, black_pieces, white_pieces)
                            check_for_stalemate(settings, black_pieces, white_pieces)
                            break
                elif settings.turn == 1:
                    for rect in white_pieces.promoting_rect:
                        if rect.collidepoint(x_pos, y_pos):
                            if white_pieces.promoting_rect.index(rect) == 0:
                                piece = "Queen"
                            if white_pieces.promoting_rect.index(rect) == 1:
                                piece = "Bishop"
                            if white_pieces.promoting_rect.index(rect) == 2:
                                piece = "Knight"
                            if white_pieces.promoting_rect.index(rect) == 3:
                                piece = "Rook"
                            white_pieces.promote(piece)
                            settings.promoting = False
                            settings.game_stats = True
                            settings.turn *= -1
                            check(settings, black_pieces, white_pieces, red_circle)
                            check_for_checkmate(settings, black_pieces, white_pieces)
                            check_for_stalemate(settings, black_pieces, white_pieces)
                            break
        if event.type == pygame.MOUSEBUTTONDOWN and settings.clicked == False and settings.game_stats == True:
            x_pos, y_pos = pygame.mouse.get_pos()
            if settings.turn == -1:
                for piece in black_pieces.pieces:
                    if piece.rect.collidepoint(x_pos, y_pos):
                        settings.piece_move = piece
                        settings.clicked = True
                        break
            if settings.turn == 1:
                for piece in white_pieces.pieces:
                    if piece.rect.collidepoint(x_pos, y_pos):
                        settings.piece_move = piece
                        settings.clicked = True
                        break
            if settings.piece_move:
                settings.piece_move.poss_moves()
                update_poss_moves(settings, black_pieces, white_pieces)
                green_circle.get_rect_circle()
        elif event.type == pygame.MOUSEBUTTONUP and settings.clicked == True and settings.game_stats == True:
            x_pos = int(settings.piece_move.rect.center[0] // settings.square)
            y_pos = int(settings.piece_move.rect.center[1] // settings.square)
            if [x_pos, y_pos] in settings.piece_move.possible_moves:
                update_casteling(settings, x_pos, y_pos)
                check_for_en_passant(settings, white_pieces, black_pieces, x_pos, y_pos)
                settings.piece_move.x= int(settings.piece_move.rect.center[0] // settings.square)
                settings.piece_move.y= int(settings.piece_move.rect.center[1] // settings.square)
                settings.moved = True
                en_passant(settings, white_pieces, black_pieces)
                casteling(settings, white_pieces, black_pieces, x_pos, y_pos)
            settings.clicked = False
            if settings.moved == False:
                settings.piece_move.pos()
                settings.piece_move = None

def update_poss_moves(settings, black_pieces, white_pieces):
    """update the possible moves of the pieces if there is a check."""
    impossible_moves = []
    x_pos = settings.piece_move.x
    y_pos = settings.piece_move.y
    if settings.turn == 1:
        check_for_white_casteling(settings, black_pieces, white_pieces)
        if settings.piece_move == settings.en_passant_pawn_1:
            settings.piece_move.possible_moves.append(settings.en_passant_pawn_pos)
        pieces = black_pieces.pieces[:]
        for move in settings.piece_move.possible_moves:
            settings.board[settings.piece_move.y][settings.piece_move.x] = 0
            settings.piece_move.x = move[0]
            settings.piece_move.y = move[1]
            update_board(settings, white_pieces, black_pieces)
            check = check_for_check(settings, black_pieces, white_pieces)
            if check == True:
                impossible_moves.append(move)
            black_pieces.pieces= pieces[:]
        settings.piece_move.x = x_pos 
        settings.piece_move.y = y_pos
        update_board(settings, white_pieces, black_pieces)
        for move in impossible_moves:
            settings.piece_move.possible_moves.remove(move)
    if settings.turn == -1:
        check_for_black_casteling(settings, black_pieces, white_pieces)
        if settings.piece_move == settings.en_passant_pawn_1:
            settings.piece_move.possible_moves.append(settings.en_passant_pawn_pos)
        pieces = white_pieces.pieces[:]
        for move in settings.piece_move.possible_moves:
            settings.board[settings.piece_move.y][settings.piece_move.x] = 0
            settings.piece_move.x = move[0]
            settings.piece_move.y = move[1]
            update_board(settings, white_pieces, black_pieces)
            check = check_for_check(settings, black_pieces, white_pieces)
            if check == True:
                impossible_moves.append(move)
            white_pieces.pieces= pieces[:]
        settings.piece_move.x = x_pos 
        settings.piece_move.y = y_pos
        update_board(settings, white_pieces, black_pieces)
        for move in impossible_moves:
            settings.piece_move.possible_moves.remove(move)
  
def check_for_check(settings, black_pieces, white_pieces):
    """check if the kings in danger"""
    if settings.turn == 1:
        for piece in black_pieces.pieces:
            if settings.piece_move.y == piece.y and settings.piece_move.x == piece.x:
                black_pieces.pieces.remove(piece)
                break
        update_board(settings, white_pieces, black_pieces)
        for piece in black_pieces.pieces:
            piece.poss_moves()
            if [white_pieces.pieces[0].x, white_pieces.pieces[0].y] in piece.possible_moves:
                return True
        return False
    if settings.turn == -1:
        for piece in white_pieces.pieces:
            if settings.piece_move.y == piece.y and settings.piece_move.x == piece.x:
                white_pieces.pieces.remove(piece)
                break
        update_board(settings, white_pieces, black_pieces)
        for piece in white_pieces.pieces:
            piece.poss_moves()
            if [black_pieces.pieces[0].x, black_pieces.pieces[0].y] in piece.possible_moves:
                return True
        return False

def check_for_checkmate(settings, black_pieces, white_pieces):
    """check if there is a checkmate if there is a check."""
    if settings.white_check == True:
        for piece in white_pieces.pieces:
            settings.piece_move = piece
            settings.piece_move.poss_moves()
            x_pos = settings.piece_move.x
            y_pos = settings.piece_move.y
            pieces = black_pieces.pieces[:]
            for move in settings.piece_move.possible_moves:
                settings.board[settings.piece_move.y][settings.piece_move.x] = 0
                settings.piece_move.x = move[0]
                settings.piece_move.y = move[1]
                update_board(settings, white_pieces, black_pieces)
                check = check_for_check(settings, black_pieces, white_pieces)
                black_pieces.pieces= pieces[:]
                if check == False:
                    settings.checkmate = False
                    break
            settings.piece_move.x = x_pos 
            settings.piece_move.y = y_pos
            update_board(settings, white_pieces, black_pieces)
            if check == False:
                settings.checkmate = False
                break
            settings.checkmate = True
        settings.piece_move = None
    if settings.black_check == True:
        for piece in black_pieces.pieces:
            settings.piece_move = piece
            settings.piece_move.poss_moves()
            x_pos = settings.piece_move.x
            y_pos = settings.piece_move.y
            pieces = white_pieces.pieces[:]
            for move in piece.possible_moves:
                settings.board[settings.piece_move.y][settings.piece_move.x] = 0
                settings.piece_move.x = move[0]
                settings.piece_move.y = move[1]
                update_board(settings, white_pieces, black_pieces)
                check = check_for_check(settings, black_pieces, white_pieces)
                white_pieces.pieces = pieces[:]
                if check == False:
                    settings.checkmate = False
                    break
            settings.piece_move.x = x_pos 
            settings.piece_move.y = y_pos
            update_board(settings, white_pieces, black_pieces)
            if check == False:
                settings.checkmate = False
                break
            settings.checkmate = True
        settings.piece_move = None

def check_for_stalemate(settings, black_pieces, white_pieces):
    """check if there is a stalemate if there is no check."""
    if settings.turn == 1:
        if settings.white_check == False:
            check = True
            for piece in white_pieces.pieces:
                settings.piece_move = piece
                settings.piece_move.poss_moves()
                x_pos = settings.piece_move.x
                y_pos = settings.piece_move.y
                pieces = black_pieces.pieces[:]
                for move in settings.piece_move.possible_moves:
                    settings.board[settings.piece_move.y][settings.piece_move.x] = 0
                    settings.piece_move.x = move[0]
                    settings.piece_move.y = move[1]
                    update_board(settings, white_pieces, black_pieces)
                    check = check_for_check(settings, black_pieces, white_pieces)
                    black_pieces.pieces= pieces[:]
                    if check == False:
                        settings.stalemate = False
                        break
                settings.piece_move.x = x_pos 
                settings.piece_move.y = y_pos
                update_board(settings, white_pieces, black_pieces)
                if check == False:
                    settings.stalemate = False
                    break
                settings.stalemate = True
            settings.piece_move = None
    if settings.turn == -1:
        if settings.black_check == False:
            check = True
            for piece in black_pieces.pieces:
                settings.piece_move = piece
                settings.piece_move.poss_moves()
                x_pos = settings.piece_move.x
                y_pos = settings.piece_move.y
                pieces = white_pieces.pieces[:]
                for move in piece.possible_moves:
                    settings.board[settings.piece_move.y][settings.piece_move.x] = 0
                    settings.piece_move.x = move[0]
                    settings.piece_move.y = move[1]
                    update_board(settings, white_pieces, black_pieces)
                    check = check_for_check(settings, black_pieces, white_pieces)
                    white_pieces.pieces = pieces[:]
                    if check == False:
                        settings.stalemate = False
                        break
                settings.piece_move.x = x_pos 
                settings.piece_move.y = y_pos
                update_board(settings, white_pieces, black_pieces)
                if check == False:
                    settings.stalemate = False
                    break
                settings.stalemate = True
            settings.piece_move = None

def update_board(settings, white_pieces, black_pieces):
    """update the board."""
    for row in range(8):
        for colomn in range(8):
            settings.board[row][colomn] = 0
    for piece in black_pieces.pieces:
        settings.board[piece.y][piece.x] = -1
    for piece in white_pieces.pieces:
        settings.board[piece.y][piece.x] = 1

def moving_piece(settings):
    """move a piece"""
    if settings.clicked == True:
        x_pos, y_pos = pygame.mouse.get_pos()
        settings.piece_move.rect.centerx = x_pos
        settings.piece_move.rect.centery = y_pos

def check_for_collisions(settings, black_pieces, white_pieces):
    """check if there is a collision between anly pieces"""
    if settings.turn == 1:
        for piece in black_pieces.pieces:
            if piece.rect.colliderect(settings.piece_move):
                black_pieces.pieces.remove(piece)
    if settings.turn == -1:
        for piece in white_pieces.pieces:
            if piece.rect.colliderect(settings.piece_move):
                white_pieces.pieces.remove(piece)
    
def check(settings, black_pieces, white_pieces,red_circle):
    """check if the kings in danger"""
    temp = 1
    settings.checking_pieces = None
    if settings.turn == 1:
        for piece in black_pieces.pieces:
            piece.poss_moves()
            if [white_pieces.pieces[0].x, white_pieces.pieces[0].y] in piece.possible_moves:
                temp = 0
                settings.white_check = True
                settings.checking_pieces = piece
                red_circle.get_pos(white_pieces.pieces[0].x, white_pieces.pieces[0].y)
    if settings.turn == -1:
        for piece in white_pieces.pieces:
            piece.poss_moves()
            if [black_pieces.pieces[0].x, black_pieces.pieces[0].y] in piece.possible_moves:
                temp = 0
                settings.black_check = True
                settings.checking_pieces =  piece
                red_circle.get_pos(black_pieces.pieces[0].x, black_pieces.pieces[0].y)
    if temp == 1:
        settings.black_check = False
        settings.white_check = False
        settings.checking_pieces = None

def turn_changer(settings, black_pieces, white_pieces,red_circle):
    """change the turn when a move is made."""
    if settings.piece_move != None and settings.clicked == False and settings.moved == True:
        settings.piece_move.pos()
        check_for_collisions(settings, black_pieces, white_pieces)
        update_board(settings, white_pieces,black_pieces)
        settings.piece_move = None
        settings.moved = False
        check_for_promote(settings, black_pieces, white_pieces)
        settings.turn *= -1
        check(settings, black_pieces, white_pieces, red_circle)
        check_for_checkmate(settings, black_pieces, white_pieces)
        check_for_stalemate(settings, black_pieces, white_pieces)
        
def check_for_promote(settings, black_pieces, white_pieces):
    """check if there is a promotion"""
    if settings.turn == 1:
        for piece in white_pieces.pieces:
            if str(piece) == "Pawn" :
                if piece.y == 0:
                    white_pieces.promoting_pawn = piece
                    settings.turn *= -1
                    settings.promoting = True
                    settings.game_stats = False 
    if settings.turn == -1:
        for piece in black_pieces.pieces:
            if str(piece) == "Pawn" :
                if piece.y == 7:
                    black_pieces.promoting_pawn = piece
                    settings.turn *= -1
                    settings.promoting = True
                    settings.game_stats = False

def check_for_white_casteling(settings, black_pieces, white_pieces):
    """check if the casteling is possible"""
    settings.white_bishop_castling = False
    settings.white_queen_castling = False
    if settings.white_castling == True:
        if settings.white_check == False and settings.turn == 1:
            king_pos = False
            rook_pos = False
            if settings.white_bishop_castling_poss == True:
                if  settings.board[7][4:] == [1, 0, 0, 1]:
                    for piece in white_pieces.pieces:
                        if str(piece) == 'King':
                            if piece.x == 4 and piece.y == 7:
                                king_pos = True
                        if str(piece) == 'Rook':
                            if piece.x == 7 and piece.y == 7:
                                rook_pos = True
                if king_pos == True and rook_pos == True:
                    if str(settings.piece_move) == 'King':
                        x_pos = settings.piece_move.x
                        y_pos = settings.piece_move.y
                        settings.piece_move.x = 5
                        settings.piece_move.y = 7
                        update_board(settings, white_pieces, black_pieces)
                        check = check_for_check(settings, black_pieces, white_pieces)
                        settings.piece_move.x = 6
                        settings.piece_move.y = 7
                        update_board(settings, white_pieces, black_pieces)
                        check = check or check_for_check(settings, black_pieces, white_pieces)
                        if check == False:
                            settings.white_bishop_castling = True
                            settings.piece_move.possible_moves.append([6, 7])
                        settings.piece_move.x = x_pos
                        settings.piece_move.y = y_pos
                        update_board(settings, white_pieces, black_pieces)
            king_pos = False
            rook_pos = False
            if settings.white_queen_castling_poss == True:
                if  settings.board[7][0:5] == [1, 0, 0, 0, 1]:
                    for piece in white_pieces.pieces:
                        if str(piece) == 'King':
                            if piece.x == 4 and piece.y == 7:
                                king_pos = True
                        if str(piece) == 'Rook':
                            if piece.x == 0 and piece.y == 7:
                                rook_pos = True
                if king_pos == True and rook_pos == True:
                    if str(settings.piece_move) == 'King':
                        x_pos = settings.piece_move.x
                        y_pos = settings.piece_move.y
                        settings.piece_move.x = 3
                        settings.piece_move.y = 7
                        update_board(settings, white_pieces, black_pieces)
                        check = check_for_check(settings, black_pieces, white_pieces)
                        settings.piece_move.x = 2
                        settings.piece_move.y = 7
                        update_board(settings, white_pieces, black_pieces)
                        check = check or check_for_check(settings, black_pieces, white_pieces)
                        if check == False:
                            settings.white_queen_castling = True
                            settings.piece_move.possible_moves.append([2, 7])
                        settings.piece_move.x = x_pos
                        settings.piece_move.y = y_pos        

def check_for_black_casteling(settings, black_pieces, white_pieces):
    """check if the casteling is possible"""
    if settings.black_castling == True:
        if settings.black_check == False and settings.turn == -1:
            king_pos = False
            rook_pos = False
            if settings.black_bishop_castling_poss == True:
                if  settings.board[0][4:] == [-1, 0, 0, -1]:
                    for piece in black_pieces.pieces:
                        if str(piece) == 'King':
                            if piece.x == 4 and piece.y == 0:
                                king_pos = True
                        if str(piece) == 'Rook':
                            if piece.x == 7 and piece.y == 0:
                                rook_pos = True
                if king_pos == True and rook_pos == True:
                    if str(settings.piece_move) == 'King':
                        x_pos = settings.piece_move.x
                        y_pos = settings.piece_move.y
                        settings.piece_move.x = 5
                        settings.piece_move.y = 0
                        update_board(settings, white_pieces, black_pieces)
                        check = check_for_check(settings, black_pieces, white_pieces)
                        settings.piece_move.x = 6
                        settings.piece_move.y = 0
                        update_board(settings, white_pieces, black_pieces)
                        check = check or check_for_check(settings, black_pieces, white_pieces)
                        if check == False:
                            settings.black_bishop_castling = True
                            settings.piece_move.possible_moves.append([6, 0])
                        settings.piece_move.x = x_pos
                        settings.piece_move.y = y_pos
                        update_board(settings, white_pieces, black_pieces)
            king_pos = False
            rook_pos = False
            if settings.black_queen_castling_poss == True:
                if  settings.board[0][0:5] == [-1, 0, 0, 0, -1]:
                    for piece in black_pieces.pieces:
                        if str(piece) == 'King':
                            if piece.x == 4 and piece.y == 0:
                                king_pos = True
                        if str(piece) == 'Rook':
                            if piece.x == 0 and piece.y == 0:
                                rook_pos = True
                if king_pos == True and rook_pos == True:
                    if str(settings.piece_move) == 'King':
                        x_pos = settings.piece_move.x
                        y_pos = settings.piece_move.y
                        settings.piece_move.x = 3
                        settings.piece_move.y = 0
                        update_board(settings, white_pieces, black_pieces)
                        check = check_for_check(settings, black_pieces, white_pieces)
                        settings.piece_move.x = 2
                        settings.piece_move.y = 0
                        update_board(settings, white_pieces, black_pieces)
                        check = check or check_for_check(settings, black_pieces, white_pieces)
                        if check == False:
                            settings.black_queen_castling = True
                            settings.piece_move.possible_moves.append([2, 0])
                        settings.piece_move.x = x_pos
                        settings.piece_move.y = y_pos
                        update_board(settings, white_pieces, black_pieces)

def casteling(settings, white_pieces, black_pieces, x_pos, y_pos):
    "change the position of the rool when a casteling is made"
    if settings.turn == 1:
        if settings.white_bishop_castling == True and str(settings.piece_move) == 'King' and [x_pos, y_pos] == [6,7]:
            for piece in white_pieces.pieces:
                if str(piece) == 'Rook' and [piece.x, piece.y] == [7, 7]:
                    piece.x = 5
                    piece.pos()
        if settings.white_queen_castling == True and str(settings.piece_move) == 'King' and [x_pos, y_pos] == [2,7]:
            for piece in white_pieces.pieces:
                if str(piece) == 'Rook' and [piece.x, piece.y] == [0, 7]:
                    piece.x = 3
                    piece.pos()
    if settings.turn == -1:
        if settings.black_bishop_castling == True and str(settings.piece_move) == 'King' and [x_pos, y_pos] == [6,0]:
            for piece in black_pieces.pieces:
                if str(piece) == 'Rook' and [piece.x, piece.y] == [7, 0]:
                    piece.x = 5
                    piece.pos()
        if settings.black_queen_castling == True and str(settings.piece_move) == 'King' and [x_pos, y_pos] == [2,0]:
            for piece in black_pieces.pieces:
                if str(piece) == 'Rook' and [piece.x, piece.y] == [0, 0]:
                    piece.x = 3
                    piece.pos()

def update_casteling(settings, x_pos, y_pos):
    """update the casteling settings"""
    if str(settings.piece_move) == "King" and settings.turn == 1 and [x_pos, y_pos] not in  [[6, 7], [2, 7]]:
        settings.white_castling = False
    if str(settings.piece_move) == "King" and settings.turn == -1 and [x_pos, y_pos] not in  [[6, 0], [2, 0]]:
        settings.black_castling = False
    if str(settings.piece_move) == "Rook" and settings.turn == 1 and [settings.piece_move.x, settings.piece_move.y] == [7, 7]:
        settings.white_bishop_castling_poss = False
    if str(settings.piece_move) == "Rook" and settings.turn == 1 and [settings.piece_move.x, settings.piece_move.y] == [0, 7]:
        settings.white_queen_castling_poss = False
    if str(settings.piece_move) == "Rook" and settings.turn == -1 and [settings.piece_move.x, settings.piece_move.y] == [7, 0]:
        settings.black_bishop_castling_poss = False
    if str(settings.piece_move) == "Rook" and settings.turn == -1 and [settings.piece_move.x, settings.piece_move.y] == [0, 0]:
        settings.black_queen_castling_poss = False

def check_for_en_passant(settings, white_pieces, black_pieces, x_pos, y_pos):
    """check if there is an en passant"""
    if str(settings.piece_move) == 'Pawn':
        if settings.turn == -1:
            if y_pos - settings.piece_move.y == 2:
                for piece in white_pieces.pieces:
                    if str(piece) == "Pawn" and piece.y == 3 and (piece.x == x_pos + 1 or piece.x == x_pos -1):
                        settings.en_passant_pawn_1 = piece
                        settings.en_passant_pawn_pos = [x_pos, y_pos - 1]
                        settings.en_passant_pawn_2 = settings.piece_move
                        settings.white_en_passant = True
        if settings.turn == 1:
            if y_pos - settings.piece_move.y == -2:
                for piece in black_pieces.pieces:
                    if str(piece) == "Pawn" and piece.y == 4  and (piece.x == x_pos + 1 or piece.x == x_pos -1):
                        settings.en_passant_pawn_1 = piece
                        settings.en_passant_pawn_pos = [x_pos, y_pos + 1]
                        settings.en_passant_pawn_2 = settings.piece_move
                        settings.black_en_passant = True
        
def en_passant(settings, white_pieces, black_pieces):
    """remove the pawn when en passant is made."""
    if settings.turn == 1:
        if settings.piece_move == settings.en_passant_pawn_1:
            if [settings.piece_move.x, settings.piece_move.y] == settings.en_passant_pawn_pos:
                black_pieces.pieces.remove(settings.en_passant_pawn_2)
        if settings.white_en_passant == True:
            settings.en_passant_pawn_1 = None
            settings.en_passant_pawn_pos = None
            settings.en_passant_pawn_2 = None
            settings.white_en_passant = False
    if settings.turn == -1:
        if settings.piece_move == settings.en_passant_pawn_1:
            if [settings.piece_move.x, settings.piece_move.y] == settings.en_passant_pawn_pos:
                white_pieces.pieces.remove(settings.en_passant_pawn_2)
        if settings.black_en_passant == True:
            settings.en_passant_pawn_1 = None
            settings.en_passant_pawn_pos = None
            settings.en_passant_pawn_2 = None
            settings.black_en_passant = False

def draw_bande(screen, settings):
    """draw the bande if the there is a checkmate."""
    if settings.checkmate == True:
        if settings.turn == 1:
            image = pygame.image.load('images/bande_white_checkmate.png')
            rect = image.get_rect()
            screen_rect = screen.get_rect()
            rect.center = screen_rect.center
            settings.game_stats = False
        if settings.turn == -1:
            image = pygame.image.load('images/bande_black_checkmate.png')
            rect = image.get_rect()
            screen_rect = screen.get_rect()
            rect.center = screen_rect.center
            settings.game_stats = False
    if settings.stalemate == True:
        image = pygame.image.load('images/stalemate.png')
        rect = image.get_rect()
        screen_rect = screen.get_rect()
        rect.center = screen_rect.center
        settings.game_stats = False
    screen.blit(image, rect)

def update_screen(screen, settings, board, black_pieces, white_pieces, green_circle, red_circle):
    """draw game parts on the screen"""
    board.get_rect_board()
    board.draw_board()
    if settings.clicked == True:
        green_circle.blitme()
    if settings.white_check == True or settings.black_check == True:
        red_circle.blitme()
    black_pieces.blitme()
    white_pieces.blitme()
    if settings.stalemate == True or settings.checkmate == True:
        draw_bande(screen, settings)
    if settings.promoting == True:
        settings.game_stats = False
        if settings.turn == -1:
            black_pieces.get_promoting()
            black_pieces.promoting_blit()
        if settings.turn == 1:
            white_pieces.get_promoting()
            white_pieces.promoting_blit()
    pygame.display.flip()