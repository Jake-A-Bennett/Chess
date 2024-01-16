import Piece

class Knight(Piece.Piece):
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