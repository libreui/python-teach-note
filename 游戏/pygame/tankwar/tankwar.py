import pygame
from pygame.sprite import Group

from settings import Settings
from tank import Tank
from resources import Resources
from map import Map


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

        # 实例化一个坦克(Test)
        self.tank = Tank(self, self.elements)


    def ran(self):
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

        self.tank.blitme()
        self.tank.bullets.update()
        self.tank.bullets.draw(self.screen)

        pygame.display.flip()

    def _update_map_elements(self):
        for ele, group in self.elements.get_elements().items():
            group.draw(self.screen)

if __name__ == "__main__":
    tw = TankWar()
    tw.ran()
