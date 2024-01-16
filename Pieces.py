import pygame
import os
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from King import King
from Queen import Queen
import Piece


class Pieces:
    def __init__(self, board, pawn_row, piece_row, piece_images, color):
        self.board = board.board
        self.color = color
        self.piece_images = piece_images
        #The x and y values are not correct
        self.pieces = {"Rook1": Rook(folder="Assets", file=piece_images["Rook"], x=0, y=0, board=self.board, color=self.color),
                       "Knight1": Knight(folder="Assets", file=piece_images["Knight"], x=0, y=0, board=self.board, color=self.color),
                       "Bishop1": Bishop(folder="Assets", file=piece_images["Bishop"], x=0, y=0, board=self.board, color=self.color),
                       "Queen": Queen(folder="Assets", file=piece_images["Queen"], x=0, y=0, board=self.board, color=self.color),
                       "King": King(folder="Assets", file=piece_images["King"], x=0, y=0, board=self.board, color=self.color),
                       "Bishop2": Bishop(folder="Assets", file=piece_images["Bishop"], x=0, y=0, board=self.board, color=self.color),
                       "Knight2": Knight(folder="Assets", file=piece_images["Knight"], x=0, y=0, board=self.board, color=self.color),
                       "Rook2": Rook(folder="Assets", file=piece_images["Rook"], x=0, y=0, board=self.board, color=self.color)}

        self.create_other_pieces(piece_row)
        self.create_pawns(pawn_row)



    def create_pawns(self, row):
        for pawn in range(8):
            self.pieces[f"Pawn{pawn}"] = Pawn(folder="Assets", file=self.piece_images["Pawn"], x=self.board[pawn][row][0].left, y=self.board[pawn][row][0].top, board=self.board, color=self.color)
            self.pieces[f"Pawn{pawn}"].square = [pawn, row]
            self.board[pawn][row][2] = self.pieces[f"Pawn{pawn}"]

    def create_other_pieces(self, row):
        count = 0
        for piece in self.pieces.values():
            piece.cur_x = self.board[count][row][0].left
            piece.cur_y = self.board[count][row][0].top
            piece.prev_x = piece.cur_x
            piece.prev_y = piece.cur_y
            piece.square = [count, row]
            self.board[count][row][2] = piece
            count += 1

    def draw_pieces(self, surface):
        for row in range(len(self.board)):
            for column in range(0, len(self.board[row])):
                square = self.board[row][column]
                x = self.pieces[f"Pawn{column}"].cur_x
                y = self.pieces[f"Pawn{column}"].cur_y
                surface.blit(source=self.pieces[f"Pawn{column}"].img, dest=(x, y))


        for piece in self.pieces.values():
            surface.blit(source=piece.img, dest=(piece.cur_x, piece.cur_y))







