import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#light
LIGHT = (232, 235, 239)
#dark
DARK = (125, 135, 150)
coordinates = list()
rectangles = dict()

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

board = Board(rows=8, columns=8, size=60, pos_x=6, pos_y=1, colors=[LIGHT, DARK])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #draws all rectangle objects to the screens
    board.draw_board(screen)

    pygame.display.flip()


clock.tick(60)
pygame.quit()

