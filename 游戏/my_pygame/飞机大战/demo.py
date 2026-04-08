import pygame
import pygame.sprite

pygame.init()
screen = pygame.display.set_mode(pygame.Rect(0, 0, 480, 700).size)
screen.fill((255, 255, 255))


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(f"./images/me{i}.png") for i in range(1, 3)]  # 加载动画序列的图像
        self.current_image = 0  # 初始图像索引

    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)  # 切换到下一帧图像


# 创建角色对象
character = Character()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    character.update()  # 更新角色的动画

    print(character.current_image)
    current_image = character.images[character.current_image]
    # 绘制角色
    screen.blit(current_image, (0, 0))

    # 刷新屏幕
    pygame.display.flip()

# 退出程序
pygame.quit()
