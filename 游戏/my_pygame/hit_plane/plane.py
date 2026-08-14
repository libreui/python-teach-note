from pygame.sprite import Sprite
import pygame


class Plane(Sprite):
    """飞机类"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.scale = 0.7

        self.image = pygame.image.load('image/plane.png')

        ori_width, ori_height = self.image.get_size()
        new_width = int(ori_width * self.scale)
        new_height = int(ori_height * self.scale)
        
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        # 重新设置矩形
        self.rect = self.image.get_rect()

        # 每艘飞机都放在屏幕底部中央
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.rect.y -= 50

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def show_plane(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.x, self.y = mouse_pos

        self.rect.center = (self.x, self.y)
