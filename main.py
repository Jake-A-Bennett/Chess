import pygame
from Board import Board
from Pieces import Pieces
from Settings import *
import os


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

piece_images_white = WHITE_PIECES_IMG
piece_images_black = BLACK_PIECES_IMG

board = Board(rows=BOARD_ROWS, columns=BOARD_COLUMNS, size=BOARD_SIZE, pos_x=BOARD_POS_X, pos_y=BOARD_POS_Y, colors=[COLORS["LIGHT"], COLORS["DARK"]])
pieces = Pieces(board=board, pawn_row=6, piece_row=7, piece_images=piece_images_white, color="White")
black_pieces = Pieces(board=board, pawn_row=1, piece_row=0, piece_images=piece_images_black, color="Black")

pressed_button = None

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

def touched_rect_cord():
    for row in range(len(board.board)):
        for column in range(len(board.board[row])):
            if board.board[row][column][0].collidepoint(pygame.mouse.get_pos()):
                return [row, column]


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_button = touched()
        if event.type == pygame.MOUSEBUTTONUP and touched() != None:
            try:
                pressed_button.valid_move(touched_rect_cord(), pressed_button)
                pressed_button.valid_move(touched_rect_cord(), pressed_button)
                board.board[pressed_button.square[0]][pressed_button.square[1]][2] = None
                board.board[touched_rect_cord()[0]][touched_rect_cord()[1]][2] = pressed_button
                pressed_button.square = touched_rect_cord()
                pressed_button.cur_x = touched_rect().left
                pressed_button.cur_y = touched_rect().top
                pressed_button.prev_x = pressed_button.cur_x
                pressed_button.prev_y = pressed_button.cur_y
            except:
                pressed_button.cur_x = pressed_button.prev_x
                pressed_button.cur_y = pressed_button.prev_y
            pressed_button = None

    if pressed_button is not None:
        pressed_button.cur_x = pygame.mouse.get_pos()[0]-25
        pressed_button.cur_y = pygame.mouse.get_pos()[1]-25


    screen.fill(FILL)
    #draws all rectangle objects to the screens
    board.draw_board(screen)
    pieces.draw_pieces(screen)
    black_pieces.draw_pieces(screen)

    pygame.display.update()

    pygame.display.flip()


clock.tick(60)
pygame.quit()

