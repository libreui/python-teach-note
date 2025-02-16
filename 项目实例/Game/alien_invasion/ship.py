import pygame


class Ship:
    def __init__(self, ai_game):
        """初始化飞船并设置其初始的属性"""
        # 获取游戏的屏幕
        self.screen = ai_game.screen
        # 获取屏幕的形状
        self.screen_rect = self.screen.get_rect()

        # 获取游戏的相关设置
        self.settings = ai_game.settings

        # 加载飞船的图片资源
        self.image = pygame.image.load('./images/ship.bmp')
        # 获取飞船的矩形数据
        self.rect = self.image.get_rect()

        # 设置飞船的初始位置
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x

        # 定义连续右移动的开关
        self.move_right = False
        self.move_left = False

    def update(self):
        """关于飞船角色的移动"""

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed


    def blitme(self):
        """绑定飞船到屏幕上"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
