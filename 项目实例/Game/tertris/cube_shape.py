import random

import pygame


class CubeShape:
    # 定义积木映射
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
         [(-1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, 1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (1, 0)]]
    L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
         [(1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, -1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (-1, 0)]]
    O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
         [(1, -1), (1, 0), (0, 0), (0, 1)]]
    T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, -1)]]
    Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
         [(-1, 0), (0, 0), (0, -1), (1, -1)]]

    SHAPES_WITH_DIR = {
        'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z
    }

    def __init__(self, tetris):
        self.screen = tetris.screen
        self.settings = tetris.settings

        self.shape = self.SHAPES_WITH_DIR[self.SHAPES[random.randint(0, len(self.SHAPES)-1)]]
        self.shape = self.shape[random.randint(0, len(self.shape) - 1)]
        # 在网格上shape中心的位置
        self.center = (1, self.settings.grid_num_width // 2)
        self.color = self.settings.cube_color[random.randint(0, len(self.settings.cube_color) - 1)]

    def get_all_gridpos(self, center=None):
        """获取所有网格坐标"""
        if center is None:
            center = self.center
        return [(cube[0] + center[0], cube[1] + center[1]) for cube in self.shape]

    def draw(self):
        """绘制积木"""

        # 绘制每个小方块(y, x)
        for cube in self.get_all_gridpos():
            # (x, y)
            pygame.draw.rect(self.screen, self.color,
                             (cube[1] * self.settings.grid_width, cube[0] * self.settings.grid_width,
                              self.settings.grid_width, self.settings.grid_width))
            pygame.draw.rect(self.screen, self.settings.white,
                             (cube[1] * self.settings.grid_width, cube[0] * self.settings.grid_width,
                              self.settings.grid_width, self.settings.grid_width), 1)
