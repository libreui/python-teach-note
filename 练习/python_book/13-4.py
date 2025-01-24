import random

import pygame
import sys
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.sprite import Group
from pygame.time import Clock

pygame.init()

screen = pygame.display.set_mode((600, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption('雨滴下落练习')
fps = 60
clock = Clock()

_rect = Rect(100, 100, 50, 50)
_rect.midbottom = screen_rect.midbottom

class Rain(Sprite):
    def __init__(self, x):
        super().__init__()
        self.rect = Rect(x, 30, 2, 4)
        self.screen = screen
        self.y = self.rect.y
        self.speed = 0

    def draw(self):
        """绘制矩形"""
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def update(self):
        """更新雨滴位置"""
        self.y += self.speed
        self.rect.y = self.y


def create_rain(x):
    r = Rain(x)
    r.y = random.randint(10, 600)
    r.speed = random.randint(10, 20)
    rains.add(r)


rains = Group()
n = 600 // 10
for i in range(1, n + 1):
    create_rain(i * 10)


while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    for rain in rains:
        rain.draw()

    for rain in rains.copy():
        # 超过屏幕底部 移除雨滴
        if rain.rect.bottom > screen_rect.bottom:
            # 保存将要消失的雨滴的X坐标
            _x = rain.rect.x
            rains.remove(rain)
            # 创建新的雨滴
            create_rain(_x)

    _rect.x = pygame.mouse.get_pos()[0]
    _rect.y = pygame.mouse.get_pos()[1]
    pygame.draw.rect(screen, (0, 0, 255), _rect)

    rains.update()

    pygame.display.update()
