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
max_balls = 10

center_x = screen_rect.centerx
center_y = screen_rect.centery

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 发射所有小球
                for i in range(max_balls):
                    if max_balls > 1:
                        angle = -45 + i * (90 / (max_balls - 1))
                    else:
                        angle = 0
                    # 计算小球的速度分量 (0度向上)
                    vx = speed * math.sin(math.radians(angle))
                    vy = -speed * math.cos(math.radians(angle))
                    balls.append([center_x, center_y, vx, vy])
    
    # 更新小球位置
    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]
    
    screen.fill(BLACK)
    # 绘制所有小球
    for ball in balls:
        pygame.draw.circle(screen, WHITE, (int(ball[0]), int(ball[1])), radius)
    pygame.display.flip()
    
    clock.tick(FPS)
