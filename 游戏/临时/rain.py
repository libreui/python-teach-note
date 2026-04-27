import math
import random
import sys

import pygame
from mpl_toolkits.mplot3d.proj3d import transform

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Rain:

    W = 800
    H = 600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption('Rain')

        self.clock = pygame.time.Clock()

        self.rains = []
        self._create_rain()


    def _create_rain(self):
        """创建雨滴"""
        for _ in range(100):
            x = random.randint(0, self.W)
            y = random.randint(0, self.H)
            s = random.randint(3, 10)
            rain = pygame.Rect(x, y, 2, 6)
            # 旋转雨滴, 已知x_speed为4, y_speed为s, 用三角函数求角度
            self.rains.append((rain, s))

    def run(self):
        while True:
            self._check_events()
            self._draw()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _draw(self):
        self.screen.fill(BLACK)

        for rain in self.rains:
            r = rain[0]
            if r.bottom > self.screen.get_rect().bottom:
                r.x = random.randint(0, self.W)
                r.y = 0
            # r.move_ip(4, rain[1])
            pygame.draw.rect(self.screen, WHITE, r)

        pygame.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    rain = Rain()
    rain.run()
