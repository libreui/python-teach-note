import pygame
from pygame.sprite import Sprite


class Elements:
    def __init__(self):
        self._groups = {
            'brick': pygame.sprite.Group(),
            'iron': pygame.sprite.Group(),
        }

    def add_brick(self, brick):
        self._groups['brick'].add(brick)

    def add_iron(self, iron):
        self._groups['iron'].add(iron)

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
