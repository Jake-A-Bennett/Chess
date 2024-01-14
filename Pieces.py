import pygame
import os

class Piece:
    def __init__(self, folder, file, x, y):
        self.img = pygame.image.load(os.path.join(folder, file))
        self.cur_x = x
        self.cur_y = y

class Pawn(Piece):
    def __init__(self, folder, file, x, y):
        super().__init__(folder, file, x, y)
class Rook(Piece):
    def __init__(self, folder, file, x, y):
        super().__init__(folder, file, x, y)

class Bishop(Piece):
        def __init__(self, folder, file, x, y):
            super().__init__(folder, file, x, y)

class Knight(Piece):
    def __init__(self, folder, file, x, y):
        super().__init__(folder, file, x, y)

class King(Piece):
    def __init__(self, folder, file, x, y):
        super().__init__(folder, file, x, y)

class Queen(Piece):
    def __init__(self, folder, file, x, y):
        super().__init__(folder, file, x, y)


class Pieces:
    def __init__(self, board, pawn_row, piece_row, piece_images):
        self.board = board.board
        self.piece_images = piece_images
        #The x and y values are not correct
        self.pieces = {"Rook1": Rook(folder="Assets", file=piece_images["Rook"], x=0, y=0),
                       "Knight1": Knight(folder="Assets", file=piece_images["Knight"], x=0, y=0),
                       "Bishop1": Bishop(folder="Assets", file=piece_images["Bishop"], x=0, y=0),
                       "Queen": Queen(folder="Assets", file=piece_images["Queen"], x=0, y=0),
                       "King": King(folder="Assets", file=piece_images["King"], x=0, y=0),
                       "Bishop2": Bishop(folder="Assets", file=piece_images["Bishop"], x=0, y=0),
                       "Knight2": Knight(folder="Assets", file=piece_images["Knight"], x=0, y=0),
                       "Rook2": Rook(folder="Assets", file=piece_images["Rook"], x=0, y=0)}

        self.create_other_pieces(piece_row)
        self.create_pawns(pawn_row)



    def create_pawns(self, row):
        for pawn in range(8):
            self.pieces[f"Pawn{pawn}"] = Pawn(folder="Assets", file=self.piece_images["Pawn"], x=self.board[pawn][row][0].left, y=self.board[pawn][row][0].top)

    def create_other_pieces(self, row):
        count = 0
        for piece in self.pieces.values():
            piece.cur_x = self.board[count][row][0].left
            piece.cur_y = self.board[count][row][0].top
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







