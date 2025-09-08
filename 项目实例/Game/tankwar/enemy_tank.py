import random

import pygame
from pygame.sprite import Sprite
from bullet import Bullet


class EnemyTank(Sprite):
    def __init__(self, tw, elements, pos=(0, 0)):
        super().__init__()

        self.frame = 0

        self.bullets = tw.bullets

        self.elements = elements
        self.settings = tw.settings
        self.screen = tw.screen
        self.screen_rect = self.screen.get_rect()
        self.res = tw.res  # 资源
        # 方向
        self.direction = self._get_direction()
        # 等级
        self.level = random.randint(0, 3)
        self.health = len(self.res.enemy_tank[self.level])
        self.tank_image = self.res.enemy_tank[self.level][self.health - 1]
        self._set_direction_image(self.direction)
        self.rect = self.image.get_rect()
        print(pos)
        self.rect.topleft = pos

        # 子弹冷却时间
        self.bullet_cooling = False
        self.bullet_cooling_time = 120
        self.bullet_cooling_count = 0


    def _set_direction_image(self, direction):
        self.tank_image = self.res.enemy_tank[self.level][self.health - 1]
        if direction == 'up':
            self.image = self.tank_image.subsurface((0, 0), (96, 48))
        elif direction == 'down':
            self.image = self.tank_image.subsurface((0, 48), (96, 48))
        elif direction == 'left':
            self.image = self.tank_image.subsurface((0, 96), (96, 48))
        elif direction == 'right':
            self.image = self.tank_image.subsurface((0, 144), (96, 48))

        self.frame += self.settings.animate_speed
        if self.frame > 1:
            self.frame = 0
        self.image = self.image.subsurface((int(self.frame) * 48, 0), (48, 48))

    def _get_direction(self):
        return random.choice(['up', 'down', 'left', 'right'])

    def update(self):
        """随机移动"""
        self._collide_screen()
        speed = (0, 0)
        if self.direction == "up":
            speed = (0, -self.settings.enemy_tank_speed)
        elif self.direction == "down":
            speed = (0, self.settings.enemy_tank_speed)
        elif self.direction == "left":
            speed = (-self.settings.enemy_tank_speed, 0)
        elif self.direction == "right":
            speed = (self.settings.enemy_tank_speed, 0)

        rect_ori = self.rect
        self.rect = self.rect.move(speed)
        if self._collide_elements():
            self.rect = rect_ori
            self.direction = self._get_direction()
            self._set_direction_image(self.direction)


        # 子弹冷
        if self.bullet_cooling:
            self.bullet_cooling_count += 1
            if self.bullet_cooling_count >= self.bullet_cooling_time:
                self.bullet_cooling = False
                self.bullet_cooling_count = 0

        self._shoot()

    def _collide_elements(self):
        """检测碰撞"""
        is_collide = False
        for ele, group in self.elements.get_elements().items():
            collied = pygame.sprite.spritecollide(self, group, False)
            if collied:
                is_collide = True
                break
        return is_collide

    def _collide_screen(self):
        """检测碰撞"""
        if self.rect.x < self.screen_rect.left:
            self.rect.left = self.screen_rect.left
            self.direction = random.choice(['up', 'down', 'right'])
        elif self.rect.x > self.screen_rect.right - self.rect.width:
            self.rect.right = self.screen_rect.right
            self.direction = random.choice(['up', 'down', 'left'])
        elif self.rect.y < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
            self.direction = random.choice(['down', 'left', 'right'])
        elif self.rect.y > self.screen_rect.bottom - self.rect.height:
            self.rect.bottom = self.screen_rect.bottom
            self.direction = random.choice(['up', 'left', 'right'])
        self._set_direction_image(self.direction)

    def _shoot(self):
        if self.bullet_cooling:
            return
        self.bullet_cooling = True
        new_bullet = Bullet(self, self.direction, self.rect.center, self)
        self.bullets.add(new_bullet)

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
