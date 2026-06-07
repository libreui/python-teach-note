import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen_rect = screen.get_rect()
pygame.display.set_caption("Diffuse")

clock = pygame.time.Clock()
FPS = 60

radius = 2  # 小球半径
speed = 2  # 小球速度
balls = []  # 小球列表，每个元素: [x, y, vx, vy]
launch_interval = 2  # 发射间隔帧数 (0.5秒 at 60FPS)
frame_count = 0
launched_count = 0
max_balls = 1

center_x = screen_rect.centerx
center_y = screen_rect.centery

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # 发射小球
    if launched_count < max_balls and frame_count % launch_interval == 0:
        # 计算发射角度，均匀分布在360度上
        angle = (launched_count * 36) % 360
        # 计算小球的速度分量
        vx = speed * math.cos(math.radians(angle))
        vy = speed * math.sin(math.radians(angle))
        balls.append([center_x, center_y, vx, vy])
        launched_count += 1
    
    # 更新小球位置
    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]
    
    screen.fill(BLACK)
    # 绘制所有小球
    for ball in balls:
        pygame.draw.circle(screen, WHITE, (int(ball[0]), int(ball[1])), radius)
    pygame.display.flip()
    
    frame_count += 1
    clock.tick(FPS)
