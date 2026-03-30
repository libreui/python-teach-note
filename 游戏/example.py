import pygame
_WIDTH = 640
_HEIGHT = 480
# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
screen_rect = screen.get_rect()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
x = 0
rect = pygame.Rect(0, 0, 100, 100)
rect.center = screen_rect.center

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # 显示当前帧率
    clock.tick(60)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, rect)

    rect.move_ip(1, 0)

    pygame.display.update()
