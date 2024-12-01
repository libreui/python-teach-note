import random

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SNAKE_BLOCK = 10
SNAKE_SPEED = 8


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, (x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK))


def get_food_position():
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_BLOCK))
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK))
    return food_x, food_y

def game_loop():

    # 初始化蛇头位置以及蛇身体每块的增量
    x1 = SCREEN_WIDTH // 2
    y1 = SCREEN_HEIGHT // 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x, food_y = get_food_position()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    print('向右移动')
                    x1_change = 1
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -1
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -1
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 1

        # 更新蛇头位置
        x1 += x1_change * SNAKE_BLOCK
        y1 += y1_change * SNAKE_BLOCK

        # 填充屏幕，准备重新绘制蛇
        screen.fill(BLACK)

        # 绘制食物
        pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK))

        # 添加蛇头
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # 绘制蛇
        draw_snake(snake_list)

        pygame.display.flip()

        # 检查是否吃掉食物
        if x1 == food_x and y1 == food_y:
            food_x, food_y = get_food_position()
            snake_length += 1

        # 控制游戏帧率
        clock.tick(SNAKE_SPEED)


game_loop()
