import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


BLUE = (0, 0, 255)
coordinates = list()
rectangles = dict()

def create_board(rows, columns, size):

    for row in range(rows):
        for column in range(columns):
            coordinates.append(((row+6)*65, (column + 1)*65, size, size))

def create_rectangles():
    for coordinate in range(len(coordinates)):
        rectangles[f"rect{coordinate}"] = pygame.Rect(coordinates[coordinate])

create_board(rows=8, columns=8, size=60)
create_rectangles()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #draws all rectangle objects to the screens
    for rectangle in rectangles.keys():
        pygame.draw.rect(surface=screen, color=BLUE, rect=rectangles[rectangle])

    pygame.display.flip()


clock.tick(60)
pygame.quit()

