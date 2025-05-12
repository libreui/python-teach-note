import time

import pygame
from pygame import Rect

import resources as res


class Tank:
    def __init__(self, tw, x=0, y=0):
        self.clock = tw.clock
        self.screen = tw.screen
        self.settings = tw.settings
        self.screen_rect = tw.screen.get_rect()

        # 加载坦克图像
        self.image = pygame.image.load(res.tank_0)

        self.timer = 0
        self.timer_max = self.settings.fps

        self.rect = Rect(x, y, 48, 48)
        self.up = [
            self.image.subsurface((0, 0, 48, 48)),
            self.image.subsurface((48, 0, 48, 48))
        ]
        self.down = [
            self.image.subsurface((0, 48, 48, 48)),
            self.image.subsurface((48, 48, 48, 48))
        ]

        self.direction = 'up'

    def blitme(self):
        self.timer += self.settings.animate_speed
        if self.timer >= len(self.up):
            self.timer = 0
        if self.direction == 'up':
            self.screen.blit(self.up[int(self.timer)], self.rect)
        if self.direction == 'down':
            self.screen.blit(self.down[int(self.timer)], self.rect)
