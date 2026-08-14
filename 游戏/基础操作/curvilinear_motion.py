import pygame
import math

# 初始化pygame
pygame.init()

# 窗口设置
WIDTH = 400
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("方块S形移动")

# 方块参数
block_size = 40
x = WIDTH // 2   # 起始水平位置
y = 0            # 起始垂直位置
speed_y = 1.2    # 向下移动速度
amplitude = 120  # S曲线左右摆动幅度
frequency = 0.018 # 波浪疏密系数
clock = pygame.time.Clock()

running = True
while running:
    # 事件监听（关闭窗口）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景，清除上一帧
    screen.fill((25, 25, 25))

    # S轨迹核心公式：利用正弦实现左右摇摆
    offset_x = amplitude * math.sin(y * frequency)
    current_x = WIDTH//2 + offset_x

    # 绘制方块 (红色方块)
    pygame.draw.rect(screen, (220, 50, 50), (current_x, y, block_size, block_size))

    # 垂直坐标持续向下
    y += speed_y

    # 如果方块到达底部，重置回到顶端循环
    if y > HEIGHT:
        y = -block_size

    pygame.display.update()
    clock.tick(60)  # 帧率60

pygame.quit()
