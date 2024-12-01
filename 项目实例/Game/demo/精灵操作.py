import random

import pygame
import sys

from pygame.sprite import Sprite


class Hero(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.x = float(random.randrange(0, 500, 60))
        self.y = float(random.randrange(0, 500, 60))

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5

    def move_up(self):
        self.y -= self.speed

    def move_left(self):
        self.x -= self.speed

    def move_down(self):
        self.y += self.speed

    def move_right(self):
        self.x += self.speed

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("精灵操作")
hero = Hero(screen)
hero_1 = Hero(screen)
hero_2 = Hero(screen)
hero_group = pygame.sprite.Group(hero_1, hero_2)


keys = {
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False


    if keys[pygame.K_UP]:
        hero.move_up()
    if keys[pygame.K_DOWN]:
        hero.move_down()
    if keys[pygame.K_LEFT]:
        hero.move_left()
    if keys[pygame.K_RIGHT]:
        hero.move_right()

    # 检测碰撞
    collections = pygame.sprite.spritecollide(hero, hero_group, True)
    if collections:
        print("碰撞了")

    hero_group.update()
    hero.update()
    screen.fill((255, 255, 255))

    # 绘制单个精灵
    screen.blit(hero.image, hero.rect)

    # 绘制多个精灵
    hero_group.update()
    hero_group.draw(screen)
    pygame.display.flip()
