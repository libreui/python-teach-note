import random

import pygame.draw


class CubeShape:
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    SHAPES_WITH_DIR = {
        'I': I
    }

    # TODO 添加其他形状

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

    def conflict(self, center):
        """检测方块是否冲突"""
        for cube in self.get_all_gridpos(center):
            # 检测是否超出边界
            if cube[0] < 0 or cube[1] < 0 or cube[0] >= self.settings.grid_num_height \
                    or cube[1] >= self.settings.grid_num_width:
                return True

            # 检测是否与已存在的方块冲突
            if self.settings.screen_color_matrix[cube[0]][cube[1]] is not None:
                return True

        return False

    def left(self):
        center = (self.center[0], self.center[1] - 1)
        if self.conflict(center):
            return False
        self.center = center
        return True

    def right(self):
        center = (self.center[0], self.center[1] + 1)
        if self.conflict(center):
            return False
        self.center = center
        return True

    def down(self):
        center = (self.center[0] + 1, self.center[1])
        if self.conflict(center):
            return False
        self.center = center
        return True

    def rotate(self):
        """旋转方块"""
        new_dir = self.dir + 1
        new_dir %= len(self.SHAPES_WITH_DIR[self.shape])
        old_dir = self.dir
        self.dir = new_dir
        if self.conflict(self.center):
            self.dir = old_dir
            return False

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
