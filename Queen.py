import Piece

class Queen(Piece.Piece):
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