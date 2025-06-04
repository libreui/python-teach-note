import pygame

WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

BLOCK_SIZE = 10
SPEED = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义蛇的长度
snake_length = 1
# 储存蛇身体的列表
snakes = []

x, y = WIDTH//2, HEIGHT//2
dx, dy = 0, 0

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -SPEED
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = SPEED
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -SPEED
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = SPEED

    # 蛇头的新坐标位置
    x += dx
    y += dy

    # 蛇头的新位置
    snake_head = [x, y]
    snakes.append(snake_head)


    screen.fill(BLACK)

    # 绘制蛇头
    for snake in snakes:
        pygame.draw.rect(screen,
                         WHITE,
                         (snake[0], snake[1], BLOCK_SIZE, BLOCK_SIZE))


    pygame.display.flip()


