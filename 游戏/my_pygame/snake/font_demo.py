import pygame

pygame.init()
screen = pygame.display.set_mode((600, 480))
clock = pygame.time.Clock()
FPS = 60

# 1. 创建文字对象
font = pygame.font.Font("./djzt.otf", size=20)


# 创建
def _crate():
    pass


# 更新坐标
def _update():
    pass


# 绘制
def _draw():
    pass


_crate()


def show_font(txt):
    # 2. 获取文字对象的render(渲染对象)
    font_render = font.render(txt, True, (255, 255, 255))
    # 3. 绘制到屏幕(Surface)
    screen.blit(font_render, font_render.get_rect())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    _update()

    _draw()
    pygame.display.flip()
    clock.tick(FPS)
