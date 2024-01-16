import pygame
import os

class Piece:
    def __init__(self, folder, file, x, y, board, color):
        self.img = pygame.image.load(os.path.join(folder, file)).convert_alpha()
        self.board = board
        self.cur_x = x
        self.cur_y = y
        self.prev_x = x
        self.prev_y = y
        self.square = None
        self.color = color