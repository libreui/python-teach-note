import pygame
from settings import Settings
from tank import Tank
import resources as res


class TankWar:
    def __init__(self):
        self.settings = Settings()
        pygame.init()
        screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("坦克大战")
        self.clock = pygame.time.Clock()

        # 加载背景图片
        self.bg_image = pygame.image.load(res.bg)

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
                pass
            elif event.type == pygame.KEYUP:
                pass

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))

        self.tank.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    tw = TankWar()
    tw.ran()
