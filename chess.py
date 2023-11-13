import pygame
from chess_settings import Settings
from board import Board
import game_functions as gf
from black_pieces import BlackPieces
from white_pieces import WhitePieces
from circles import *


settings = Settings()
def run_game():
    """The main function of the game."""
    # Initializing pygame.
    pygame.init()
    # creating the screen.
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_width))
    pygame.display.set_caption("Chess")
    # make board.
    board = Board(screen, settings)
    # Make black pices.
    black_pieces = BlackPieces(screen, settings, board)
    # Make white pices.
    white_pieces = WhitePieces(screen, settings, board)
    # Make green circles.
    green_circle = GreenCircle(screen, settings, board)
    # Make green circles.
    red_circle = RedCircle(screen, settings, board)
    gf.update_board(settings, white_pieces, black_pieces)
    # Start the main loop of the game.
    while True:
        gf.check_events(settings, black_pieces, white_pieces, green_circle, red_circle)
        gf.moving_piece(settings)
        gf.turn_changer(settings, black_pieces, white_pieces, red_circle)
        gf.update_screen(screen, settings, board, black_pieces, white_pieces, green_circle, red_circle)

run_game()