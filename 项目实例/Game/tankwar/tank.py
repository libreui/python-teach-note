import time

import pygame
from pygame import Rect
from pygame.sprite import Sprite

import resources as res


class Tank(Sprite):
    def __init__(self, tw, x=0, y=0):
        super().__init__()
        self.clock = tw.clock
        self.screen = tw.screen
        self.settings = tw.settings
        self.screen_rect = tw.screen.get_rect()
        self.res = tw.res

        # 加载坦克图像
        self.tank_image = self.res.tank_0
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

    def move(self, direction, elements):
        self.direction = direction
        speed = (0, 0)
        if direction == 'up':
            speed = (0, -self.settings.tank_speed)
        elif direction == 'down':
            speed = (0, self.settings.tank_speed)
        elif direction == 'left':
            speed = (-self.settings.tank_speed, 0)
        elif direction == 'right':
            speed = (self.settings.tank_speed, 0)
        rect_ori = self.rect.copy()
        self.rect = self.rect.move(speed)
        # 检测碰到物体
        for ele, group in elements.get_elements().items():
            collied = pygame.sprite.spritecollide(self, group, False)
            if collied:
                self.rect = rect_ori
        # 检测碰撞
        self.collide_window(rect_ori)

    def collide_window(self, rect_ori):
        """碰撞检测"""
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
