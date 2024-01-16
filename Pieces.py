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

class Pawn(Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)
        self.move = 0


    def valid_move(self, cord, cur_piece):
        if cur_piece.color == "White":
            piece = self.board[cord[0]][cord[1]][2]
            if cord[1] + 1 == self.square[1] and cord[0] == self.square[0] and piece is None:
                return True
            else:
                raise "Invalid move for pawn"
        elif cur_piece.color == "Black" and self.move > 1:
            piece = self.board[cord[0]][cord[1]][2]
            if cord[1] - 1 == self.square[1] and cord[0] == self.square[0] and piece is None:
                return True
            else:
                raise "Invalid move for pawn"
class Rook(Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)

    def valid_move(self, cord, cur_piece):
        valid_moves = list()
        piece = self.board[cord[0]][cord[1]][2]

        for i in range(cur_piece.square[1]-1, -1, -1):
            other_piece = self.board[self.square[0]][i][2]
            try:
                if other_piece is None:
                    valid_moves.append([self.square[0], i])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[1]+1, 8):
            other_piece = self.board[self.square[0]][i][2]
            try:
                if other_piece is None:
                    valid_moves.append([self.square[0], i])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[0]+1, 8):
            other_piece = self.board[i][self.square[1]][2]
            try:
                if other_piece is None:
                    valid_moves.append([i, self.square[1]])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[0]-1, -1, -1):
            other_piece = self.board[i][self.square[1]][2]
            try:
                if other_piece is None:
                    valid_moves.append([i, self.square[1]])
                else:
                    break
            except:
                pass



        if cord in valid_moves and piece is None:
            return True
        else:
            raise "This does not work"



class Bishop(Piece):
        def __init__(self, folder, file, x, y, board, color):
            super().__init__(folder, file, x, y, board, color)

        def valid_move(self, cord, cur_piece):
            valid_moves = list()
            piece = self.board[cord[0]][cord[1]][2]
            for i in range(1, 8):
                try:
                    if self.board[self.square[0]+i][self.square[1]+i][2] is None:
                        valid_moves.append([self.square[0]+i, self.square[1]+i])
                    else:
                        break
                except:
                    pass
#
            for i in range(1, 8):
                try:
                    if self.board[self.square[0]-i][self.square[1]-i][2] is None:
                        valid_moves.append([self.square[0]-i, self.square[1]-i])
                    else:
                        break
                except:
                    pass
#
            for i in range(1, 8):
                try:
                    if self.board[self.square[0]-i][self.square[1]+i][2] is None:
                        valid_moves.append([self.square[0]-i, self.square[1]+i])
                    else:
                        break
                except:
                    pass

            for i in range(1, 8):
                try:
                    if self.board[self.square[0]+i][self.square[1]-i][2] is None:
                        valid_moves.append([self.square[0] + i, self.square[1] - i])
                    else:
                        break
                except:
                    pass

            if cord in valid_moves and piece is None:
                return True
            else:
                raise "Not a vaild move"



class Knight(Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)

    def valid_move(self, cord, cur_piece):
        piece = self.board[cord[0]][cord[1]][2]

        try:
            if piece.color == "Black":
                return True
        except:
            pass

        if cord[0] + 2 == self.square[0] and cord[1] + 1 == self.square[1] and piece is None: return True
        if cord[0] + 2 == self.square[0] and cord[1] - 1 == self.square[1] and piece is None: return True
        if cord[0] - 2 == self.square[0] and cord[1] + 1 == self.square[1] and piece is None: return True
        if cord[0] - 2 == self.square[0] and cord[1] - 1 == self.square[1] and piece is None: return True
        if cord[0] + 1 == self.square[0] and cord[1] + 2 == self.square[1] and piece is None: return True
        if cord[0] + 1 == self.square[0] and cord[1] - 2 == self.square[1] and piece is None: return True
        if cord[0] - 1 == self.square[0] and cord[1] + 2 == self.square[1] and piece is None: return True
        if cord[0] - 1 == self.square[0] and cord[1] - 2 == self.square[1] and piece is None: return True

        raise "this does not work"



class King(Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)
        self.board = board
    def valid_move(self, cord, cur_piece):
        piece = self.board[cord[0]][cord[1]][2]
        if cord[1] + 1 == self.square[1] and cord[0] == self.square[0] and piece is None: return True
        if cord[1] - 1 == self.square[1] and cord[0] == self.square[0] and piece is None: return True
        if cord[1] + 1 == self.square[1] and cord[0] + 1 == self.square[0] and piece is None: return True
        if cord[1] - 1 == self.square[1] and cord[0] - 1 == self.square[0] and piece is None: return True
        if cord[1] + 1 == self.square[1] and cord[0] - 1 == self.square[0] and piece is None: return True
        if cord[1] - 1 == self.square[1] and cord[0] + 1 == self.square[0] and piece is None: return True
        if cord[1] == self.square[1] and cord[0] + 1 == self.square[0] and piece is None: return True
        if cord[1] == self.square[1] and cord[0] - 1 == self.square[0] and piece is None: return True

        raise "does not work"

class Queen(Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)

    def valid_move(self, cord, cur_piece):
        valid_moves = list()
        piece = self.board[cord[0]][cord[1]][2]
        for i in range(cur_piece.square[1]-1, -1, -1):
            other_piece = self.board[self.square[0]][i][2]
            try:
                if other_piece is None:
                    valid_moves.append([self.square[0], i])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[1]+1, 8):
            other_piece = self.board[self.square[0]][i][2]
            try:
                if other_piece is None:
                    valid_moves.append([self.square[0], i])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[0]+1, 8):
            other_piece = self.board[i][self.square[1]][2]
            try:
                if other_piece is None:
                    valid_moves.append([i, self.square[1]])
                else:
                    break
            except:
                pass

        for i in range(cur_piece.square[0]-1, -1, -1):
            other_piece = self.board[i][self.square[1]][2]
            try:
                if other_piece is None:
                    valid_moves.append([i, self.square[1]])
                else:
                    break
            except:
                pass

        for i in range(1, 8):
            try:
                if self.board[self.square[0] + i][self.square[1] + i][2] is None:
                    valid_moves.append([self.square[0] + i, self.square[1] + i])
                else:
                    break
            except:
                pass
        #
        for i in range(1, 8):
            try:
                if self.board[self.square[0] - i][self.square[1] - i][2] is None:
                    valid_moves.append([self.square[0] - i, self.square[1] - i])
                else:
                    break
            except:
                pass
        #
        for i in range(1, 8):
            try:
                if self.board[self.square[0] - i][self.square[1] + i][2] is None:
                    valid_moves.append([self.square[0] - i, self.square[1] + i])
                else:
                    break
            except:
                pass

        for i in range(1, 8):
            try:
                if self.board[self.square[0] + i][self.square[1] - i][2] is None:
                    valid_moves.append([self.square[0] + i, self.square[1] - i])
                else:
                    break
            except:
                pass

        if cord in valid_moves and piece is None:
            return True
        else:
            raise "Not a vaild move"




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







