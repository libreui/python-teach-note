import pygame
from pygame import Rect
from pygame.sprite import Sprite

# 坦克位置
tank_pos = [0, 0]


class Elements:
    def __init__(self):
        self._groups = {
            'brick': pygame.sprite.Group()
        }

    def add_brick(self, brick):
        self._groups['brick'].add(brick)

    def get_elements(self):
        return self._groups


class Brick(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Iron(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
