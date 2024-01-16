import Piece


class Bishop(Piece.Piece):
    def __init__(self, folder, file, x, y, board, color):
        super().__init__(folder, file, x, y, board, color)

    def valid_move(self, cord, cur_piece):
        valid_moves = list()
        piece = self.board[cord[0]][cord[1]][2]
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