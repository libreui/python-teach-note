import random

import pygame
from pygame.sprite import Sprite
from bullet import Bullet


class EnemyTank(Sprite):
    def __init__(self, tw, pos=(0, 0)):
        super().__init__()
        self.screen = tw.screen
        self.screen_rect = self.screen.get_rect()
        self.frame = 0

        # 出生动画相关设置
        self.is_appear = False
        self.appear_frame = 0
        self.appear_count = 0

        self.tw = tw
        self.map = tw.map
        self.res = tw.res
        self.elements = tw.elements
        self.settings = tw.settings
        self.direction = self._get_direction()
        # 等级
        self.level = random.randint(0, 3)
        self.health = len(self.res.enemy_tank[self.level])
        self.tank_image = self.res.enemy_tank[self.level][self.health - 1]
        self._get_direction_image()
        self.rect = self.image.get_rect()

        self.bullets = tw.bullets

        # 子弹冷却时间
        self.bullet_cooling = False
        self.bullet_cooling_time = 120
        self.bullet_cooling_count = 0



    def _appear_animate(self):
        if self.is_appear:
            return
        self.appear_frame += self.settings.animate_speed
        if self.appear_frame > 3:
            self.appear_frame = 0

        self.appear_count += 1
        if self.appear_count > 60:
            self.is_appear = True
            return

        self.image = self.res.appear.subsurface((int(self.appear_frame) * 48, 0), (48, 48))



    def _get_direction(self):
        return random.choice(['up', 'down', 'left', 'right'])

    def _get_direction_image(self):

        if not self.is_appear:
            self._appear_animate()
            return

        self.tank_image = self.res.enemy_tank[self.level][self.health - 1]
        if self.direction == 'up':
            self.image = self.tank_image.subsurface((0, 0), (96, 48))
        elif self.direction == 'down':
            self.image = self.tank_image.subsurface((0, 48), (96, 48))
        elif self.direction == 'left':
            self.image = self.tank_image.subsurface((0, 96), (96, 48))
        elif self.direction == 'right':
            self.image = self.tank_image.subsurface((0, 144), (96, 48))

        self.frame += self.settings.animate_speed
        if self.frame > 1:
            self.frame = 0
        self.image = self.image.subsurface((int(self.frame) * 48, 0), (48, 48))

    def update(self):
        """随机移动"""
        self._get_direction_image()
        if not self.is_appear:
            return
        speed = 0
        direction = self.direction
        if direction == 'up':
            speed = (0, -self.settings.tank_speed)
        elif direction == 'down':
            speed = (0, self.settings.tank_speed)
        elif direction == 'left':
            speed = (-self.settings.tank_speed, 0)
        elif direction == 'right':
            speed = (self.settings.tank_speed, 0)

        rect_ori = self.rect
        self.rect = self.rect.move(speed)
        if (self._check_collied_screen()
                or self._check_collied_elements()):
            self.rect = rect_ori



        # 子弹冷
        if self.bullet_cooling:
            self.bullet_cooling_count += 1
            if self.bullet_cooling_count >= self.bullet_cooling_time:
                self.bullet_cooling = False
                self.bullet_cooling_count = 0

        self._shoot()

    def _check_collied_screen(self):
        if (self.rect.left < self.screen_rect.left
                or self.rect.right > self.screen_rect.right
                or self.rect.top < self.screen_rect.top
                or self.rect.bottom > self.screen_rect.bottom):
            self.direction = self._get_direction()  # 重新设置方向
            return True

    def _check_collied_elements(self):
        for ele, group in self.elements.get_elements().items():
            if pygame.sprite.spritecollideany(self, group):
                self.direction = self._get_direction()  # 重新设置方向
                return True


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


