import pygame
import random
import time
from pygame.locals import *

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

sound_1 = pygame.mixer.Sound("assets/sounds/shot_sound.wav")

clock = pygame.time.Clock()
FPS = 100

bloodImage = pygame.image.load('assets/images/zombie_blood.png')
gunImage = pygame.image.load('assets/images/gun_1.png')

mainBg = pygame.image.load("assets/images/main_bg.jpg")

def startScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(mainBg, (0, 0))

        pygame.display.update()

def bloodPatch(posX, posY):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(bloodImage, (posX - 50, posY - 50))
        pygame.display.update()
        clock.tick(10)
        break

def timer(s):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Time Left : "+str(s), True, red)
    screen.blit(text, (10,10))

def gameOver():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over", True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text, (100, 100))

        pygame.display.update()

def game():
    zombieImage = random.choice(zombieList)
    zombie_x = random.randint(0, width - zombieImage.get_width())
    zombie_y = random.randint(0, height - zombieImage.get_height())
    pygame.time.set_timer(USEREVENT + 1, 1000)
    seconds = 10
    gunY = height - 250

    while True:

        posX, posY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1
                # print(seconds)

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_1.play()
                gunY -= 40
                if gun_rect.colliderect(zombie_rect):
                    # pygame.image.load('assets/images/zombie_blood.png')
                    # time.sleep(2)
                    # pygame.time.wait(2000)
                    zombieImage = random.choice(zombieList)
                    zombie_x = random.randint(0, width - zombieImage.get_width())
                    zombie_y = random.randint(0, height - zombieImage.get_height())
                    bloodPatch(posX, posY)
            else:
                gunY = height - 250

        screen.fill(blue)
        screen.blit(img_1, (0,0))
        screen.blit(zombieImage, (zombie_x, zombie_y))
        screen.blit(pointer, (posX - 50, posY - 50))
        screen.blit(gunImage, (posX, gunY))

        gun_rect = pygame.Rect(posX - 50, posY - 50, pointer.get_width(), pointer.get_height())
        zombie_rect = pygame.Rect(zombie_x, zombie_y, zombieImage.get_width(), zombieImage.get_height())

        if seconds == 0:
            gameOver()
            break

        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

# game()
startScreen()