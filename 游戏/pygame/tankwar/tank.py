import pygame
from pygame import Rect
from pygame.sprite import Group
from bullet import Bullet


class Tank:
    def __init__(self, tw, elements, x=0, y=0):
        self.tw = tw
        self.map = tw.map
        self.elements = elements
        self.clock = tw.clock
        self.screen = tw.screen
        self.settings = tw.settings
        self.screen_rect = tw.screen.get_rect()
        self.res = tw.res

        # 加载坦克图像
        self.image = self.res.tank_0

        self.timer = 0
        self.timer_max = self.settings.fps

        self.rect = Rect(self.map.tank_pos, (48, 48))
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

        self.bullets = tw.bullets

        # 子弹冷却时间
        self.bullet_cooling = False
        self.bullet_cooling_time = 60
        self.bullet_cooling_count = 0

    def move(self, direction):
        speed = 0
        self.direction = direction
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


    def _check_collied_elements(self):
        is_collied = False
        for ele, group in self.elements.get_elements().items():
            collisions = pygame.sprite.spritecollide(self, group, False)
            if collisions:
                is_collied = True
                break
        return is_collied

    def fire(self):
        self._remove_bullet()
        if self.bullet_cooling:
            return
        new_bullet = Bullet(self.tw, self.direction, self.rect.center, self)
        self.bullets.add(new_bullet)
        self.bullet_cooling = True

    def _remove_bullet(self):
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0
                    or bullet.rect.top >= self.screen_rect.height
                    or bullet.rect.right <= 0
                    or bullet.rect.left >= self.screen_rect.width):
                self.bullets.remove(bullet)

    def _check_collied_screen(self):
        is_collied = False
        if self.rect.x < 0:
            self.rect.x = 0
            is_collied = True
        if self.rect.x > self.screen_rect.width - self.settings.tank_size:
            self.rect.x = self.screen_rect.width - self.settings.tank_size
            is_collied = True
        if self.rect.y < 0:
            self.rect.y = 0
            is_collied = True
        if self.rect.y > self.screen_rect.height - self.settings.tank_size:
            self.rect.y = self.screen_rect.height - self.settings.tank_size
            is_collied = True
        return is_collied

    def update(self):
        # 子弹冷
        if self.bullet_cooling:
            self.bullet_cooling_count += 1
            if self.bullet_cooling_count >= self.bullet_cooling_time:
                self.bullet_cooling = False
                self.bullet_cooling_count = 0

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
