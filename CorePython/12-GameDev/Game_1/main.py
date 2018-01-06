import pygame
import random

pygame.init()

blue = 0,0,255
red = 255,0,0

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

img_1 = pygame.image.load("assets/images/background.png")
pointer = pygame.image.load("assets/images/aim_pointer.png")

zombie_1 = pygame.image.load("assets/images/zombie_1.gif")
zombie_2 = pygame.image.load("assets/images/zombie_2.png")
zombie_3 = pygame.image.load("assets/images/zombie_3.png")
zombie_4 = pygame.image.load("assets/images/zombie_4.png")

zombieList = [zombie_1, zombie_2, zombie_3, zombie_4]

zombieImage = random.choice(zombieList)

sound_1 = pygame.mixer.Sound("assets/sounds/shot_sound.wav")

clock = pygame.time.Clock()
FPS = 100

zombie_x = random.randint(0, width - zombieImage.get_width())
zombie_y = random.randint(0, height - zombieImage.get_height())

while True:

    posX, posY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            sound_1.play()

    screen.fill(blue)
    screen.blit(img_1, (0,0))
    screen.blit(zombieImage, (zombie_x, zombie_y))
    screen.blit(pointer, (posX - 50, posY - 50))

    pygame.display.update()
    clock.tick(FPS)
