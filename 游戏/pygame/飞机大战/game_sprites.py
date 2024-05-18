import random

import pygame.sprite

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.animate_speed = 0.1

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类方法，设置image & speed
        super().__init__("./images/me1.png", 0)
        self.images = [pygame.image.load(f"./images/me{i}.png") for i in range(1, 3)]
        self.current_image = 0

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 80
        # 创建字典精灵对象
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.current_image += self.animate_speed
        if self.current_image >= len(self.images):
            self.current_image = 0
        # self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[int(self.current_image)]
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.y = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        """开火"""
        pass


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 判断是否飞出屏幕，如果飞出屏幕从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕，需要从精灵组中删除...")
            # kill方法可以删除
            self.kill()

    def __del__(self):
        print("敌机挂了...%s" % self.rect)
