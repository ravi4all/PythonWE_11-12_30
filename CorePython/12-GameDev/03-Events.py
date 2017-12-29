import pygame

pygame.init()

blue = 0,0,255

screen = pygame.display.set_mode((900,600))

while True:

##    ev = pygame.event.get()
##    print(ev)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(blue)

    pygame.display.update()
