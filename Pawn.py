import Piece

class Pawn(Piece.Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)
        self.move = 1


    def valid_move(self, cord, cur_piece):

        if cur_piece.color == "White":
            piece = self.board[cord[0]][cord[1]][2]
            if cord[1] + 1 == self.square[1] and cord[0] == self.square[0] and piece is None:
                self.move += 1
                return True
            else:
                raise "Invalid move for pawn"
        elif cur_piece.color == "Black":
            piece = self.board[cord[0]][cord[1]][2]
            if cord[1] - 1 == self.square[1] and cord[0] == self.square[0] and piece is None:
                self.move += 1
                return True
            else:
                raise "Invalid move for pawn"