import pygame


# 初始化Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Manual Physics in Pygame')
clock = pygame.time.Clock()

# 物体属性
x = 400
y = 100
radius = 20
velocity_y = 0
gravity = 0.5
floor_height = 500


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 应用重力
    velocity_y += gravity
    y += velocity_y

    # 碰撞检测（与地面碰撞）
    if y + radius >= floor_height:
        y = floor_height - radius
        velocity_y = -velocity_y * 0.8  # 反弹并损失部分能量

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
