import pygame
from pygame import Rect
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, tw, direction, pos=(0, 0), owner=None):
        super().__init__()
        self.tw = tw
        self.screen = tw.screen
        self.settings = tw.settings
        self.res = tw.res
        self.rect = Rect(0, 0, 12, 12)
        self.rect.center = pos
        self.direction = direction
        self.image = self.get_image()
        self.owner = owner

    def get_image(self):
        image = self.res.bullet_up
        if self.direction == 'down':
            image = self.res.bullet_down
        elif self.direction == 'left':
            image = self.res.bullet_left
        elif self.direction == 'right':
            image = self.res.bullet_right
        return image

    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.settings.bullet_speed
        elif self.direction == 'down':
            self.rect.y += self.settings.bullet_speed
        elif self.direction == 'left':
            self.rect.x -= self.settings.bullet_speed
        elif self.direction == 'right':
            self.rect.x += self.settings.bullet_speed




