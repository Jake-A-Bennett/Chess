import Piece

class King(Piece.Piece):
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