import random
import time

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

PIRPLE = 145, 25, 130
BLACK = 0, 0, 0
RED = 205, 201, 10
RGB = 250, 10, 10
GREEN = 10, 255, 10
BEIGE = 10, 200, 50
WHITE = 255, 255, 255

FPS = pygame.time.Clock()

pygame.init()

font = pygame.font.SysFont('Verdana', 20)
screen = width, height = 1000, 780
main_surfase = pygame.display.set_mode(screen)

#player = pygame.image.load('player.png').convert_alpha()
#player_rect = player.get_rect()
#player_speed = 10

ball = pygame.Surface((30, 30))
ball.fill((PIRPLE))
ball_rect = ball.get_rect()
ball_speed = 6

def create_eneny():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RGB)
    enemy_rest = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 10)
    return [enemy, enemy_rest, enemy_speed]

def create_bonus():
    bonus = pygame.Surface((15, 15))
    bonus.fill((GREEN))
    bonus_rest = pygame.Rect(random.randint(0, width),0, *bonus.get_size())
    bonus_speed = random.randint(1, 20)
    return [bonus, bonus_rest, bonus_speed]


bg = pygame.transform.scale(pygame.image.load('images/background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1000)

enemies = []
bonus_spis = []

point = 0
is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_eneny())

        if event.type == CREATE_BONUS:
            bonus_spis.append(create_bonus())

    pressed_keys = pygame.key.get_pressed()

    #main_surfase.fill((WHITE))

    #main_surfase.blit(bg, (0, 0))

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surfase.blit(bg, (bgX, 0))
    main_surfase.blit(bg, (bgX2, 0))






    main_surfase.blit(ball, ball_rect)



    main_surfase.blit(font.render(str(point), True, BEIGE), (width - 30 , 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surfase.blit(enemy[0], enemy[1])
        if enemy[1].left < 0:                        #ENEMY
            enemies.pop(enemies.index(enemy))
        if ball_rect.colliderect(enemy[1]):
            time.sleep(2)
            print('Your point = ', point)
            if point >= 10:
                print('You have won')
            is_working = False



    for bonys in bonus_spis:
        bonys[1] = bonys[1].move(0, bonys[2])
        main_surfase.blit(bonys[0], bonys[1])
        if bonys[1].bottom > height:
            bonus_spis.pop(bonus_spis.index(bonys))
        if ball_rect.colliderect(bonys[1]):
            bonus_spis.pop(bonus_spis.index(bonys))
            point += 1



    if pressed_keys[K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT] and ball_rect.right <= width:
        ball_rect = ball_rect.move(ball_speed, 0 )

    if pressed_keys[K_LEFT] and ball_rect.left >= 0:
        ball_rect = ball_rect.move(-ball_speed, 0 )



    pygame.display.flip()