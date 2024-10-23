import sys
import pygame
import os

from settings import Settings
from game_stats import GameStats
from cube_shape import CubeShape


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.fps = self.settings.fps

        self.cube = None

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.__check_event()
            self.__update_screen()

            # TODO左右移动积木

    def __draw_grids(self):
        """绘制网格"""
        # 绘制竖线
        for i in range(self.settings.grid_num_width):
            pygame.draw.line(self.screen,
                             self.settings.line_color,
                             (i * self.settings.grid_width, 0),
                             (i * self.settings.grid_width, self.settings.height))

        # 绘制横线
        for i in range(self.settings.grid_num_height):
            pygame.draw.line(self.screen,
                             self.settings.line_color,
                             (0, i * self.settings.grid_width),
                             (self.settings.width, i * self.settings.grid_width))

        # 绘制边界
        pygame.draw.line(self.screen,
                         self.settings.line_color,
                         (self.settings.grid_width * self.settings.grid_num_width, 0),
                         (self.settings.grid_width * self.settings.grid_num_width, self.settings.height))

    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not self.stats.cube_active:
                    self.stats.cube_active = True
                    self.cube = CubeShape(self)
                    break
                if event.key == pygame.K_SPACE:
                    self.cube.rotate()

    def __update_screen(self):
        self.screen.fill(self.settings.black)
        self.__draw_grids()
        if self.cube is not None:
            self.cube.draw()
        pygame.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
