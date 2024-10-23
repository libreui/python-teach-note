import random

import pygame.draw


class CubeShape:
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    SHAPES_WITH_DIR = {
        'I': I
    }

    def __init__(self, tetris):
        """创建方块"""
        self.screen = tetris.screen
        self.settings = tetris.settings
        self.stats = tetris.stats

        # self.shape = self.SHAPES[random.randint(0, len(self.SHAPES) - 1)]
        self.shape = self.SHAPES[0]
        self.center = (1, self.settings.grid_num_width // 2)
        self.dir = random.randint(0, len(self.SHAPES_WITH_DIR[self.shape]) - 1)
        self.color = self.settings.cube_color[random.randint(0, len(self.settings.cube_color) - 1)]

    def get_all_gridpos(self, center=None):
        """获取方块所有网格坐标"""
        curr_shape = self.SHAPES_WITH_DIR[self.shape][self.dir]
        if center is None:
            center = self.center
        return [(cube[0] + center[0], cube[1] + center[1]) for cube in curr_shape]

    def rotate(self):
        """旋转方块"""
        self.dir = (self.dir + 1) % len(self.SHAPES_WITH_DIR[self.shape])

    def draw(self):
        """绘制方块"""
        for cube in self.get_all_gridpos():
            pygame.draw.rect(
                self.screen, self.color,
                (cube[1] * self.settings.grid_width, cube[0] * self.settings.grid_width,
                 self.settings.grid_width, self.settings.grid_width)
            )
            pygame.draw.rect(
                self.screen, self.settings.white,
                (cube[1] * self.settings.grid_width, cube[0] * self.settings.grid_width,
                 self.settings.grid_width, self.settings.grid_width),
                1
            )

