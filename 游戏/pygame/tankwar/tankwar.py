import pygame
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

        # 实例化一个坦克(Test)
        self.tank = Tank(self)

        # 初始化一个地图
        self.elements = Map(self).load_map("level_0.lvl")


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
                self._check_tank_events(event)
            elif event.type == pygame.KEYUP:
                self.tank.dx = 0
                self.tank.dy = 0

    def _check_tank_events(self, event):
        if event.key == pygame.K_UP:
            self.tank.dy -= self.settings.tank_speed
            self.tank.direction = 'up'
        if event.key == pygame.K_DOWN:
            self.tank.dy += self.settings.tank_speed
            self.tank.direction = 'down'
        if event.key == pygame.K_LEFT:
            self.tank.dx -= self.settings.tank_speed
            self.tank.direction = 'left'
        if event.key == pygame.K_RIGHT:
            self.tank.dx += self.settings.tank_speed
            self.tank.direction = 'right'

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))

        self._update_map_elements()

        self.tank.blitme()
        self.tank.update()

        pygame.display.flip()

    def _update_map_elements(self):
        for ele, group in self.elements.get_elements().items():
            group.draw(self.screen)

if __name__ == "__main__":
    tw = TankWar()
    tw.ran()
