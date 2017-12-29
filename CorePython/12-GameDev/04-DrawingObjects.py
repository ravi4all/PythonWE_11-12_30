import pygame

pygame.init()

blue = 0,0,255
red = 255,0,0

screen = pygame.display.set_mode((900,600))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(blue)
    # [x,y,width,height]
    pygame.draw.rect(screen,red,[10,12,50,55])

    pygame.draw.circle(screen,red,[300,300],100)

    pygame.display.update()
