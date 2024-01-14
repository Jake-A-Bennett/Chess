import pygame
from Board import Board
from Pieces import Pieces
import os


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#light
LIGHT = (232, 235, 239)
#dark
DARK = (125, 135, 150)

piece_images_white = {"Rook": "Chess_rlt60.png",
                "Bishop": "Chess_blt60.png",
                "Knight": "Chess_nlt60.png",
                "Queen": "Chess_qlt60.png",
                "King": "Chess_klt60.png",
                "Pawn": "Chess_plt60 (1).png"}

piece_images_black = {"Rook": "Chess_rdt60.png",
                "Bishop": "Chess_bdt60.png",
                "Knight": "Chess_ndt60.png",
                "Queen": "Chess_qdt60.png",
                "King": "Chess_kdt60.png",
                "Pawn": "Chess_pdt60.png"}



board = Board(rows=8, columns=8, size=60, pos_x=6, pos_y=1, colors=[LIGHT, DARK])
pieces = Pieces(board=board, pawn_row=6, piece_row=7, piece_images=piece_images_white)
black_pieces = Pieces(board=board, pawn_row=1, piece_row=0, piece_images=piece_images_black)

def touched():
    for piece in pieces.pieces.values():
        rect = piece.img.get_rect(x=piece.cur_x, y=piece.cur_y)
        if rect.collidepoint(pygame.mouse.get_pos()):
            return piece

    for piece in black_pieces.pieces.values():
        rect = piece.img.get_rect(x=piece.cur_x, y=piece.cur_y)
        if rect.collidepoint(pygame.mouse.get_pos()):
            return piece



def touched_rect():
    for row in board.board:
        for column in row:
            if column[0].collidepoint(pygame.mouse.get_pos()):
                return column[0]

while running:

    buttons = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif buttons[0] and touched() is not None:
            touched().cur_x = pygame.mouse.get_pos()[0] - 25
            touched().cur_y = pygame.mouse.get_pos()[1] - 25
        elif not buttons[0] and touched() is not None:
            touched().cur_x = touched_rect().left
            touched().cur_y = touched_rect().top



    screen.fill("black")
    #draws all rectangle objects to the screens
    board.draw_board(screen)
    pieces.draw_pieces(screen)
    black_pieces.draw_pieces(screen)

    pygame.display.update()

    pygame.display.flip()


clock.tick(60)
pygame.quit()

