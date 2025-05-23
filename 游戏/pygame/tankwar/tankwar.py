import pygame
from pygame.sprite import Group

from settings import Settings
from tank import Tank
from resources import Resources
from map import Map
from enemy_tank import EnemyTank
from elements import Iron, Brick
from audio import Audio


class TankWar:
    def __init__(self):
        self.settings = Settings()
        pygame.init()
        screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("坦克大战")
        self.clock = pygame.time.Clock()

        self.res = Resources()

        self.audio = Audio(self)

        # 加载背景图片
        self.bg_image = self.res.bg

        # 初始化一个地图
        self.map = Map(self)
        self.elements = self.map.load_map("level_0.lvl")

        # 子弹的编组
        self.bullets = Group()

        # 实例化一个坦克(Test)
        self.tank = Tank(self, self.elements)

        # 实例化一个敌人坦克编组
        self.enemy_tanks = Group()
        self.enemy_tanks.add(EnemyTank(self, self.elements))


    def get_tank(self):
        return self.tank

    def get_enemy_tanks(self):
        return self.enemy_tanks

    def get_elements(self):
        return self.elements


    def ran(self):
        self.audio.start()
        while True:
            self._check_events()
            self._check_tank_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank.fire()

    def _check_tank_events(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.tank.move('up')
        elif key_pressed[pygame.K_DOWN]:
            self.tank.move('down')
        elif key_pressed[pygame.K_LEFT]:
            self.tank.move('left')
        elif key_pressed[pygame.K_RIGHT]:
            self.tank.move('right')



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))

        self._update_map_elements()

        # 坦克
        self.tank.update()
        self.tank.blitme()

        # 子弹
        self.bullets.update()
        self._check_bullet_collied()
        self.bullets.draw(self.screen)


        self.enemy_tanks.update()
        self.enemy_tanks.draw(self.screen)

        pygame.display.flip()

    def _update_map_elements(self):
        for ele, group in self.elements.get_elements().items():
            group.draw(self.screen)

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

        # 然后是和敌人坦克碰撞
        collections = pygame.sprite.groupcollide(self.bullets, self.enemy_tanks, False, False)
        if collections:
            for bullet, enemy_tanks in collections.items():
                if isinstance(bullet.owner, Tank) and isinstance(enemy_tanks[0], EnemyTank):
                    bullet.kill()
                    enemy_tanks[0].hit()

        # 子弹和子弹碰撞
        def bullet_collision(sprite1, sprite2):
            # 避免子弹与自身碰撞
            return sprite1 != sprite2 and pygame.sprite.collide_rect(sprite1, sprite2)

        pygame.sprite.groupcollide(self.bullets,
                                   self.bullets,
                                   True, True,
                                   collided=bullet_collision)

if __name__ == "__main__":
    tw = TankWar()
    tw.ran()
