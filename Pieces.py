import pygame
import os

#doesn't work when being drawed on top of the board class which it needs to


class Pawn:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class Rook:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class Bishop:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class Knight:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class King:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class Queen:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y


class Pieces():
    def __init__(self, board):
        self.board = board.board
        self.pieces = {"Rook1": Rook(folder="Assets", file="Chess_rdt60.png", x=10, y=0),
                       "Rook2": Rook(folder="Assets", file="Chess_rdt60.png", x=20, y=0),
                       "Knight1": Knight(folder="Assets", file="Chess_ndt60.png", x=30, y=0),
                       "Knight2": Knight(folder="Assets", file="Chess_ndt60.png", x=40, y=0),
                       "Bishop1": Bishop(folder="Assets", file="Chess_bdt60.png", x=50, y=0),
                       "Bishop2": Bishop(folder="Assets", file="Chess_bdt60.png", x=60, y=0),
                       "King": King(folder="Assets", file="Chess_kdt60.png", x=70, y=0),
                       "Queen": Queen(folder="Assets", file="Chess_qdt60.png", x=80, y=0)}



    def create_pawns(self):
        for pawn in range(8):
            self.pieces[f"Pawn{pawn}"] = Pawn(folder="Assets", file="Chess_pdt60.png", x=pawn, y=pawn)

    def draw_pieces(self, surface):
        for row in range(len(self.board)):
            for column in range(len(self.board)-2, len(self.board[row])-1):
                square = self.board[row][column]

                surface.blit(source=self.pieces[f"Pawn{column}"].img, dest=square[0])

        surface.blit(source=self.pieces["Rook1"].img, dest=self.board[0][7][0])
        surface.blit(source=self.pieces["Rook2"].img, dest=self.board[7][7][0])
        surface.blit(source=self.pieces["Knight1"].img, dest=self.board[1][7][0])
        surface.blit(source=self.pieces["Knight2"].img, dest=self.board[6][7][0])
        surface.blit(source=self.pieces["Bishop1"].img, dest=self.board[2][7][0])
        surface.blit(source=self.pieces["Bishop2"].img, dest=self.board[5][7][0])
        surface.blit(source=self.pieces["Queen"].img, dest=self.board[3][7][0])
        surface.blit(source=self.pieces["King"].img, dest=self.board[4][7][0])







