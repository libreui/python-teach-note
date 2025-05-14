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
        self.res = tw.res

        # 加载坦克图像
        self.image = self.res.tank_0

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
        self.left = [
            self.image.subsurface((0, 96, 48, 48)),
            self.image.subsurface((48, 96, 48, 48))
        ]
        self.right = [
            self.image.subsurface((0, 144, 48, 48)),
            self.image.subsurface((48, 144, 48, 48))
        ]

        self.direction = 'up'
        self.dx = 0
        self.dy = 0

    def update(self):
        """移动坦克"""
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= self.screen_rect.width - self.settings.tank_size:
            self.rect.x = self.screen_rect.width - self.settings.tank_size
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= self.screen_rect.height - self.settings.tank_size:
            self.rect.y = self.screen_rect.height - self.settings.tank_size


    def blitme(self):
        self.timer += self.settings.animate_speed
        if self.timer >= len(self.up):
            self.timer = 0
        if self.direction == 'up':
            self.screen.blit(self.up[int(self.timer)], self.rect)
        if self.direction == 'down':
            self.screen.blit(self.down[int(self.timer)], self.rect)
        if self.direction == 'left':
            self.screen.blit(self.left[int(self.timer)], self.rect)
        if self.direction == 'right':
            self.screen.blit(self.right[int(self.timer)], self.rect)
