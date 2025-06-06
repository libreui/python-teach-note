import pygame
from pygame import Rect
from pygame.sprite import Sprite

tank_pos = (0, 0)   # 玩家坦克的位置
home_pos = (0, 0)   # 家的位置
enemy_tank_pos = [] # 敌人坦克的位置


class Elements:
    def __init__(self):
        self._groups = {
            'brick': pygame.sprite.Group(),
            'iron': pygame.sprite.Group(),
            'home': pygame.sprite.Group(),
        }

    def add_brick(self, brick):
        self._groups['brick'].add(brick)

    def add_iron(self, iron):
        self._groups['iron'].add(iron)

    def add_home(self, home):
        self._groups['home'].add(home)

    def get_elements(self):
        return self._groups


class Brick(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos


class Home(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos


class Iron(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos


class ICE(Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.image = pygame.Surface((24, 24))
        self.rect = self.image.get_rect()
        for i in range(2):
            for j in range(2):
                self.image.blit(surface, (i * 12, j * 12))
        self.rect.left, self.rect.top = pos
