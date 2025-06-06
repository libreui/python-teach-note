import pygame
from pygame.sprite import Group

from settings import Settings
from tank import Tank
from resources import Resources
from map import Map
from bullet import Bullet
from enemy_tank import EnemyTank
from elements import *


class TankWar:
    def __init__(self):
        self.settings = Settings()
        pygame.init()
        screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("坦克大战")
        self.clock = pygame.time.Clock()

        self.res = Resources()
        # 加载背景图片
        self.bg_image = self.res.bg

        # 初始化一个地图
        self.elements = Map(self).load_map("level_0.lvl")

        # 实例化子弹编组
        self.bullets = Group()

        # 实例化一个坦克(Test)
        self.tank = Tank(self, self.elements)

        # 创建一个坦克编组
        self.enemy_tanks = Group()

    def get_tank(self):
        return self.tank

    def get_enemy_tanks(self):
        return self.enemy_tanks

    def get_map_elements(self):
        return self.elements.get_elements()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank.shoot()

    def _refresh_enemy_tanks(self):
        """刷新敌人坦克"""
        if len(self.enemy_tanks) > 0:
            return
        # 生产
        for pos in self.elements.enemy_tank_pos:
            enemy_tank = EnemyTank(self, self.elements, pos)
            self.enemy_tanks.add(enemy_tank)

    def _update_bullets(self):
        # 如果超出屏幕移除子弹
        for bullet in self.bullets.copy():
            if (bullet.rect.x < self.screen.get_rect().left
                    or bullet.rect.x > self.screen.get_rect().right
                    or bullet.rect.y < self.screen.get_rect().top
                    or bullet.rect.y > self.screen.get_rect().bottom):
                self.bullets.remove(bullet)
        self.bullets.update()
        self.bullets.draw(self.screen)

    def _check_tank_events(self, event=""):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.tank.move('up', self.elements)
        elif key_pressed[pygame.K_DOWN]:
            self.tank.move('down', self.elements)
        elif key_pressed[pygame.K_LEFT]:
            self.tank.move('left', self.elements)
        elif key_pressed[pygame.K_RIGHT]:
            self.tank.move('right', self.elements)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))

        self._update_map_elements()

        # 坦克
        self.tank.update()
        self.tank.blitme()
        self._check_tank_events()


        # 敌人坦克
        self._refresh_enemy_tanks()
        self.enemy_tanks.update()
        self.enemy_tanks.draw(self.screen)

        # 子弹
        self._check_bullet_collied()
        self._update_bullets()

        pygame.display.flip()

    def _update_map_elements(self):
        for ele, group in self.elements.get_elements().items():
            group.draw(self.screen)

    def _check_collied_elements(self):
        """检测碰撞地图中元素"""
        for ele, group in self.elements.get_elements().items():
            pre_x = self.tank.rect.x
            pre_y = self.tank.rect.y
            collied = pygame.sprite.spritecollide(self.tank, group, False)
            if collied:
                # 碰撞发生，将坦克位置回退到碰撞前的位置
                # 碰撞发生，将坦克位置回退到碰撞前的位置
                self.tank.rect.x = pre_x
                self.tank.rect.y = pre_y
                # 重置移动速度，阻止坦克继续移动
                self.tank.dx = 0
                self.tank.dy = 0

    def _check_bullet_collied(self):
        # 首先是和地图元素碰撞
        for ele, group in self.elements.get_elements().items():
            collections = pygame.sprite.groupcollide(self.bullets, group, True, False)
            if collections:
                for bullet, elements in collections.items():
                    if isinstance(elements[0], Iron):
                        bullet.kill()
                    elif isinstance(elements[0], Brick):
                        elements[0].kill()
            collections = pygame.sprite.groupcollide(self.bullets, self.enemy_tanks, False, False)
            if collections:
                for bullet, enemy_tanks in collections.items():
                    if isinstance(bullet.owner, Tank) and isinstance(enemy_tanks[0], EnemyTank):
                        bullet.kill()
                        enemy_tanks[0].hit()


if __name__ == "__main__":
    tw = TankWar()
    tw.run()
