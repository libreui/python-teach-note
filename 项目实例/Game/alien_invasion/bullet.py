from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self, ai_game):
        """子弹的初始化方法"""
        super().__init__() # 执行父类的初始化方法

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 创建子弹的矩形对象
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 创建y坐标位置
        self.y = float(self.rect.y)


    def update(self):
        """子弹的移动"""
        self.y -= self.settings.bullet_speed
        # 把新的y坐标付给子弹的矩形对象
        self.rect.y = self.y

    def draw_bullet(self):
        """再屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)



