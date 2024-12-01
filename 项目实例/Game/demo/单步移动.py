import pygame
import sys

# 初始化 pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("矩形和圆的移动游戏")

# 矩形的初始位置和大小
rect = pygame.Rect(100, 100, 50, 50)
# 圆的初始位置和半径
circle_center = [300, 300]
circle_radius = 25

# 移动速度
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-speed, 0)
                circle_center[0] -= speed
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(speed, 0)
                circle_center[0] += speed
            elif event.type == pygame.K_UP:
                rect.move_ip(0, -speed)
                circle_center[1] -= speed
            elif event.type == pygame.K_DOWN:
                rect.move_ip(0, speed)
                circle_center[1] += speed

    # 填充屏幕背景
    screen.fill((255, 255, 255))
    # 绘制矩形
    pygame.draw.rect(screen, (0, 0, 255), rect)
    # 绘制圆
    pygame.draw.circle(screen, (255, 0, 0), circle_center, circle_radius)
    # 更新屏幕显示
    pygame.display.flip()
