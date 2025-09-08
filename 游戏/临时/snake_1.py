import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLOCK_SIZE = 10
SPEED = 10

# 定义蛇的长度
snake_length = 20
# 储存蛇身体的列表
"""
[
    0 => [x1, y1],
    1 => [x2, y2],
    2 => [x3, y3],
    ....
    head => [x, y]
]
[1,2,3,4,5,6,7,8,9,10]
"""
snakes = []

x = 300
y = 300

# 方向
direction = ""

while True:
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

    if direction == 'left':
        x -= 10
    elif direction == 'right':
        x += 10
    elif direction == 'up':
        y -= 10
    elif direction == 'down':
        y += 10

    snake_head = [x, y]
    snakes.append(snake_head)

    screen.fill(BLACK)

    for snake in snakes:
        pygame.draw.rect(screen, WHITE, (snake[0], snake[1], BLOCK_SIZE, BLOCK_SIZE))

    if len(snakes) >= snake_length:
        del snakes[0]


    pygame.display.update()
    clock.tick(SPEED)
