from play_module import *

# 初始化游戏
pygame.init()

# 设置窗口大小
screen_size = (480, 700)
screen = pygame.display.set_mode(screen_size)

# 背景
bg_img = pygame.image.load("images/background.png")
screen.blit(bg_img, (0, 0))

pygame.display.set_caption("飞机大战")

# 初始化玩家飞机
player = Player(0, 0)

# 游戏运行
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 渲染玩儿家
    player.draw(screen)

    pygame.display.update()

pygame.quit()
