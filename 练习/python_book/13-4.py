import pygame
import sys
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.sprite import Group

pygame.init()

screen = pygame.display.set_mode((600, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption('雨滴下落练习')

class Rain(Sprite):
    def __init__(self, x):
        super().__init__()
        self.rect = Rect(x, 30, 2, 4)
        self.screen = screen

    def draw(self):
        """绘制矩形"""
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


rains = Group()
n = 600 // 10
for i in range(1, n+1):
    _rain = Rain(i * 10)
    rains.add(_rain)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for rain in rains.sprites():
        rain.draw()

    pygame.display.flip()
