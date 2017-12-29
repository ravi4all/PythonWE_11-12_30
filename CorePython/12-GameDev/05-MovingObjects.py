import pygame

pygame.init()

blue = 0,0,255
red = 255,0,0

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

x = 100
y = 50

move_x = 5
move_y = 5

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(blue)

    pygame.draw.circle(screen,red,[x,y],50)

    x += move_x
    y += move_y

    if x >= width:
        move_x = -5
    elif x < 0:
        move_x = 5
    elif y >= height:
        move_y = -5
    elif y < 0:
        move_y = 5

    pygame.display.update()
    clock.tick(FPS)
