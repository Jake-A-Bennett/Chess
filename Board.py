import pygame


class Board():
    def __init__(self, rows, columns, size, pos_x, pos_y, colors):
        self.board = [[0 for column in range(columns)] for row in range(rows)]
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.create_board(colors)

    def create_board(self, colors):
        color = colors
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if row % 2 == 0:
                    if column % 2 == 0:
                        color = colors[0]
                    else:
                        color = colors[1]
                else:
                    if column % 2 == 0:
                        color = colors[1]
                    else:
                        color = colors[0]

                coordinate = ((row+self.pos_x)*self.size, (column + self.pos_y)*self.size, self.size, self.size)
                self.board[row][column] = [coordinate, color]

    def draw_board(self, surface):
        for row in range(len(self.board)):
            for column in range(len(self.board)):
                pygame.draw.rect(surface=surface, color=self.board[row][column][1], rect=self.board[row][column][0])