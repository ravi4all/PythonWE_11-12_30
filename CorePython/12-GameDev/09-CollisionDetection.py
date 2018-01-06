import pygame
import random

pygame.init()

blue = 0,0,255
red = 255,0,0
white = 255,255,255

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

apple = pygame.image.load("apple.png")

clock = pygame.time.Clock()

def score(counter):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score "+str(counter), True, red)
    screen.blit(text, (10,10))

def snake(snakeList):
    for s in snakeList:
        pygame.draw.rect(screen, blue, (s[0], s[1], 50,50))


def game():
    x = 100
    y = 50

    move_x = 0
    move_y = 0

    snake_width = 50
    snakeList = []
    snakeLength = 1

    apple_x = random.randint(0, width - apple.get_width())
    apple_y = random.randint(0, height - apple.get_height())

    counter = 0
    
    FPS = 100
    gameLoop = True 

    while gameLoop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = 5
                    move_x = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -5
                    move_y = 0
                elif event.key == pygame.K_UP:
                    move_y = -5
                    move_x = 0

        screen.fill(white)
        screen.blit(apple, (apple_x, apple_y))

        rect_1 = [x,y,50,50]
        # rect_1 = pygame.draw.rect(screen, red, [x, y, snake_width, 50])
        rect_2 = pygame.Rect(apple_x, apple_y, apple.get_width(), apple.get_height())

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            #print(snakeList)
            del snakeList[0]

        # snakeList[:-1]

        snake(snakeList)

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                print("Game Over")
                gameLoop = False

        if rect_2.colliderect(rect_1):
            apple_x = random.randint(0, width - apple.get_width())
            apple_y = random.randint(0, height - apple.get_height())
            snakeLength += 1
            FPS += 1
            counter += 1


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

        score(counter)

        pygame.display.update()
        clock.tick(FPS)

game()
