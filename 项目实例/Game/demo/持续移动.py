import pygame
import sys

# 初始化 pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("持续移动方块")

# 方块的初始位置和大小
rect = pygame.Rect(100, 100, 50, 50)
# 方块的移动速度
speed = 5

# 存储方向键的状态
keys = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False

    # 根据按键状态更新方块位置
    if keys[pygame.K_LEFT]:
        rect.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT]:
        rect.move_ip(speed, 0)
    if keys[pygame.K_UP]:
        rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN]:
        rect.move_ip(0, speed)

    # 填充屏幕背景
    screen.fill((255, 255, 255))
    # 绘制方块
    pygame.draw.rect(screen, (0, 0, 255), rect)
    # 更新屏幕显示
    pygame.display.flip()
