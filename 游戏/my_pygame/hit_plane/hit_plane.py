import math

import pygame
from plane import Plane
from settings import Settings
from bullets import Bullet
from enemys import Enemys
from map import Map
from level import Level
from enemy_bullets import EnemyBullet


class HitPlane:

    def __init__(self):
        self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )
        self.sr = self.screen.get_rect()
        pygame.display.set_caption("Plane Hit")
        self.plane = Plane(self)

        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.enemys_bullets = pygame.sprite.Group()
        self.bullets_fire_type = 'line'

        self.map = Map(self)

        # 加载关数据
        self.level = Level(self)

        # 计时器
        self.timer = 0
        self.bullets_timer = 0

    def run_game(self):
        while True:
            self._check_events()

            # 更新计时器
            self._update_timer()

            self._create_enemy()

            self.map.update()
            self._update_plane()
            self._update_bullets()
            self._update_enemys()
            self._update_enemy_bullets()
            self._update_screen()

            self.clock.tick(self.settings.fps)

    def _update_timer(self):
        self.timer += 1
        self.level.trigger_event(self.timer // 60)
        self.bullets_timer += 1

    def _update_enemys(self):
        for enemy in self.enemys.sprites().copy():
            enemy.update()
            if enemy.check_edge():
                self.enemys.remove(enemy)

            # 更新敌机发射子弹
            self._update_enemys_fire(enemy)


    def _update_enemy_bullets(self):
        for enemy_bullet in self.enemys_bullets.sprites():
            enemy_bullet.update()

    def _update_bullets(self):
        self.bullets.update()

        # 删除超出屏幕的子弹
        for bullet in self.bullets.sprites().copy():
            if bullet.check_edge():
                self.bullets.remove(bullet)

        # 检查子弹是否与敌人碰撞
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemys, True, False)
        # 检查碰到敌人的血量，如果血量为0，删除敌人
        for enemy in collisions.values():
            for e in enemy:
                e.hit()

    def _update_screen(self):
        self.screen.fill((20, 20, 20))
        self.map.show_map()
        self.plane.show_plane()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for enemy in self.enemys.sprites():
            enemy.draw_enemy()
        for enemy_bullet in self.enemys_bullets.sprites():
            enemy_bullet.show_bullet()


        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _update_plane(self):
        self.plane.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_enemy(self):
        """创建敌人"""
        event = self.level.get_current_event()
        if event is None:
            return

        # 创建敌人,根据事件类型
        enemys = []
        # if event['type'] == 'enemy_wave':
        params = event['params']
        count = params['count']
        for i in range(params['count']):
            new_enemy = Enemys(self)
            new_enemy.set_movement(params['movement'])
            new_enemy.set_size(params['size'])
            new_enemy.set_position(i, count, params['position'])
            new_enemy.set_health(params['health'])
            new_enemy.set_bullets(params['bullets'])
            enemys.append(new_enemy)
        self.enemys.add(enemys)
        self.level.complete_event()


    def _update_enemys_fire(self, enemy):
        """发射子弹"""
        if self.bullets_timer % 200 != 0:
            return

        # 以正下方(90°)为中心，相邻子弹间隔 15° 对称分布
        # (n=1 时 offset=0 → 垂直向下，即单发)
        n = enemy.bullets_num
        for i in range(n):
            bullet = EnemyBullet(enemy)
            offset = (i - (n - 1) / 2) * 15
            angle = math.radians(90 + offset)
            bullet.dx = math.cos(angle) * self.settings.enemy_bullet_speed
            bullet.dy = math.sin(angle) * self.settings.enemy_bullet_speed
            self.enemys_bullets.add(bullet)
        enemy.bullets_num = 0
        self.bullets_timer = 0




if __name__ == "__main__":
    plane_hit = HitPlane()
    plane_hit.run_game()
