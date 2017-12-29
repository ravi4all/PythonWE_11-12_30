import pygame
import random

pygame.init()

blue = 0,0,255
red = 255,0,0

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

x = 100
y = 50

move_x = 5
move_y = 5

img_1 = pygame.image.load("background.png")

clock = pygame.time.Clock()
FPS = 100

rand_x = random.randint(-5,5)
rand_y = random.randint(-5,5)

while True:

    posX, posY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # move_x = rand_x
            # move_y = rand_y
            x = posX
            y = posY
            # rand_x = random.randint(-5,5)
            # rand_y = random.randint(-5,5)

    screen.fill(blue)
    screen.blit(img_1, (0,0))
    pygame.draw.rect(screen,red,[x,y,50,50])

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
