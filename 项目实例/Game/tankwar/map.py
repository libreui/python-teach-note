from elements import *


class Map:
    def __init__(self, tw):
        self.screen = tw.screen
        self.res = tw.res
        self.settings = tw.settings

        self.elements = Elements()

    def load_map(self, map_name):
        with open(f"resources/maps/{map_name}.lvl", "r") as f:
            self._parse_map(f)
        return self.elements

    def _parse_map(self, file):
        """解析地图文件"""
        index = -1
        for row in file.readlines():
            if row.startswith('#'):
                continue
            elif row.startswith('%'):
                continue
            else:
                index += 1
                self._parse_row(row, index)

    def _parse_row(self, row, index):
        for col, char in enumerate(row.split(' ')):
            pos = (col * self.settings.element_size,
                   index * self.settings.element_size)
            if char == 'B':
                self.elements.add_brick(Brick(pos, self.res.brick))

