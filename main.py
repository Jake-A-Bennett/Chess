import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


BLUE = (0, 0, 255)
RED = (255, 0, 0)
coordinates = list()
rectangles = dict()
def create_board(rows, columns, size, posx, posy, spacing):
    for column in range(columns):
        for row in range(rows):
            coordinates.append(((row+posx)*spacing, (column + posy)*spacing, size, size))

def create_rectangles():
    for coordinate in range(len(coordinates)):
        rectangles[f"rect{coordinate}"] = pygame.Rect(coordinates[coordinate])

#This is ugly but it works for now
def draw_board(colors):
    color = colors[0]
    count = 0
    switch = 0
    num_switch = 0
    for rectangle in rectangles.keys():
        if count == 0:
            color = colors[0]
            count += 1
        else:
            color = colors[1]
            count -= 1
        switch += 1
        if switch == 8:
            if num_switch == 0:
                count += 1
                switch = 0
                num_switch = 1
            else:
                count -= 1
                switch = 0
                num_switch = 0


        pygame.draw.rect(surface=screen, color=color, rect=rectangles[rectangle])






create_board(rows=8, columns=8, size=60, posx=6, posy=1, spacing=65)
create_rectangles()
for rectangle in rectangles.keys():
    print(rectangles[rectangle])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #draws all rectangle objects to the screens
    draw_board([RED, BLUE])

    pygame.display.flip()


clock.tick(60)
pygame.quit()

