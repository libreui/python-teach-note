import pygame


class Ship:
    def __init__(self, ai_game):
        """初始化飞船并设置其初始的属性"""
        # 获取游戏的屏幕
        self.screen = ai_game.screen
        # 获取屏幕的形状
        self.screen_rect = self.screen.get_rect()

        # 加载飞船的图片资源
        self.image = pygame.image.load('./images/ship.bmp')
        # 获取飞船的矩形数据
        self.rect = self.image.get_rect()

        # 设置飞船的初始位置
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """绑定飞船到屏幕上"""
        self.screen.blit(self.image, self.rect)
