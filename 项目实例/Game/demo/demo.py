import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("平移")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

speed = 10

circle_pos = [400, 300]  # 圆的初始位置
# rect_pos = [100, 100, 130, 130]
rect = pygame.Rect(100, 100, 50, 50)

# 创建右方向移动开关
IS_RIGHT = False
# 定义总开关
keys = {
    pygame.K_RIGHT: False,
    pygame.K_LEFT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False
}

while True:

    # 设置帧率
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # 按键按下
            keys[event.key] = True
        elif event.type == pygame.KEYUP: # 按键抬起事件
            keys[event.key] = False



    # 改变矩形的x坐标
    if keys[pygame.K_RIGHT]:
        rect.move_ip((speed, 0))
    elif keys[pygame.K_LEFT]:
        rect.move_ip((-speed, 0))
    elif keys[pygame.K_DOWN]:
        rect.move_ip((0, speed))
    elif keys[pygame.K_UP]:
        rect.move_ip((0, -speed))


    # 填充屏幕
    screen.fill(WHITE)

    # 绘制一个矩形
    pygame.draw.rect(screen, BLACK, rect)


    # 更新屏幕
    pygame.display.flip()
