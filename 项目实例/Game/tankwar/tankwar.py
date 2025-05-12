import pygame
from settings import Settings
from tank import Tank
from resources import Resources
from map import Map


class TankWar:
    def __init__(self):
        self.settings = Settings()
        self.res = Resources()
        pygame.init()
        screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("坦克大战")
        self.clock = pygame.time.Clock()

        # 加载背景图片
        self.bg_image = self.res.bg

        # 加载地图场景
        self.elements = Map(self).load_map('level_0')
        print(self.elements)

        # 实例化一个坦克(Test)
        self.tank = Tank(self)


    def ran(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.tank.dx = -self.settings.tank_speed
                    self.tank.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.tank.dx = self.settings.tank_speed
                    self.tank.direction = 'right'
                elif event.key == pygame.K_UP:
                    self.tank.dy = -self.settings.tank_speed
                    self.tank.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.tank.dy = self.settings.tank_speed
                    self.tank.direction = 'down'
            elif event.type == pygame.KEYUP:
                self.tank.dx = 0
                self.tank.dy = 0

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))

        self.tank.blitme()
        self.tank.update()

        self._update_map()

        pygame.display.flip()


    def _update_map(self):
        for k, group in self.elements.get_elements().items():
            group.draw(self.screen)



if __name__ == "__main__":
    tw = TankWar()
    tw.ran()
