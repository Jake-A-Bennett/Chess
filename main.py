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


board = Board(rows=8, columns=8, size=60, pos_x=6, pos_y=1, colors=[LIGHT, DARK])
pieces = Pieces(board=board)
pieces.create_pawns()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    #draws all rectangle objects to the screens
    board.draw_board(screen)
    pieces.draw_pieces(screen)

    pygame.display.update()

    pygame.display.flip()


clock.tick(60)
pygame.quit()

