import random

import pygame

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SNAKE_BLOCK = 10
FPS = 10
snake_list = [] # [x, y]
snake_length = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

x_change = 0
y_change = 0

direction = ""



def draw_snake(snakes):
    for x in snakes:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

def food_position():
    x = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
    y = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
    return [x, y]


def events():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'

def set_direction():
    global x_change, y_change
    if direction == 'left':
        x_change += -1
        y_change += 0
    elif direction == 'right':
        x_change += 1
        y_change += 0
    elif direction == 'up':
        x_change += 0
        y_change += -1
    elif direction == 'down':
        x_change += 0
        y_change += 1


food_x, food_y = food_position()

while True:

    events()
    set_direction()

    screen.fill(BLACK)

    head = [x_change * SNAKE_BLOCK, y_change * SNAKE_BLOCK]
    snake_list.append(head)

    draw_snake(snake_list)

    if len(snake_list) >= snake_length:
        del snake_list[0]

    pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

    if head[0] == food_x and head[1] == food_y:
        food_x, food_y = food_position()
        snake_length += 1

    pygame.display.update()

    clock.tick(FPS)
