import pygame
import sys

# 初始化
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((600, 480))
# 设置窗体标题
pygame.display.set_caption("游戏测试")

# 设置时钟
clock = pygame.time.Clock()

# 设置背景颜色 (R, G, B) 0-255
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
gold = (255, 215, 0)
screen.fill(gold)


def draw_line(star, end):
    """绘制一条直线"""
    pygame.draw.line(screen, black, star, end)


for i in range(0, 600, 10):
    draw_line((i, 0), (i, 480))

# 绘制矩形
rect = pygame.draw.rect(screen, red, [50, 50, 100, 100])


# 在屏幕上绘制文字
font = pygame.font.SysFont("SimHei", 60)
font_img = font.render("Hello Pygame", True, white)
screen.blit(font_img, (200, 200))
print(font_img.get_rect().y)

font_1 = pygame.font.SysFont("SimHei", 30)
font_img_1 = font_1.render("Hello Pygame", True, white)
font_img_1_rect = font_img_1.get_rect()
font_img_1_rect.top = font_img.get_rect().bottom + 10
screen.blit(font_img_1, font_img_1_rect)

while True:
    clock.tick(30)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                print('向左移动')
            elif event.key == pygame.K_RIGHT:
                print('向右移动')
            elif event.key == pygame.K_UP:
                print('向上移动')
            elif event.key == pygame.K_DOWN:
                print('向下移动')

    font_img_1.get_rect().y += 10
    pygame.display.flip()

    # pygame.display.update()
