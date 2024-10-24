import sys
import pygame
from pprint import pprint

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
            self.__pin_cube()
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
                elif event.key == pygame.K_LEFT:
                    self.cube.left()
                elif event.key == pygame.K_RIGHT:
                    self.cube.right()
                elif event.key == pygame.K_DOWN:
                    while self.cube.down():
                        pass

    def __pin_cube(self):
        if self.stats.cube_active and self.stats.counter % self.settings.fps == 0:
            if not self.cube.down():
                for cube in self.cube.get_all_gridpos():
                    self.settings.screen_color_matrix[cube[0]][cube[1]] = self.cube.color
                self.cube = CubeShape(self)
                # 判断是否已经到屏幕顶端，需要清楚屏幕方块
                if self.cube.conflict(self.cube.center):
                    self.stats.cube_active = False
                    self.cube = None
                    self.settings.screen_color_matrix = [[None] * self.settings.grid_num_width for _ in range(self.settings.grid_num_height)]
        self.stats.counter += 1

    def __draw_matrix(self):
        """绘制堆积方块"""
        for i, row in zip(range(self.settings.grid_num_height), self.settings.screen_color_matrix):
            for j, color in zip(range(self.settings.grid_num_width), row):
                if color is not None:
                    pygame.draw.rect(self.screen, color,
                                     (j * self.settings.grid_width, i * self.settings.grid_width,
                                      self.settings.grid_width, self.settings.grid_width))
                    pygame.draw.rect(self.screen, self.settings.white,
                                     (j * self.settings.grid_width, i * self.settings.grid_width,
                                      self.settings.grid_width, self.settings.grid_width), 1)

    def __update_screen(self):
        self.screen.fill(self.settings.black)
        self.__draw_grids()
        self.__draw_matrix()
        if self.cube is not None:
            self.cube.draw()
        pygame.display.update()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
