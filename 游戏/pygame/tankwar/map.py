import os
from elements import *


class Map:
    def __init__(self, tw):
        self.settings = tw.settings
        self.elements = Elements()
        self.res = tw.res
        self.path = os.path.dirname(__file__) + "/resources/maps"


    def load_map(self, map_name):
        """加载地图文件"""
        with open(self.path + "/" + map_name, "r") as f:
            file = f.readlines()
            self._parse_map_file(file)

        return self.elements


    def _parse_map_file(self, file):
        """解析文件"""
        y = -1
        for row in file:
            """解析行"""
            if row.startswith("#"):
                pass
            elif row.startswith("%"):
                if row.startswith("%PLAYERTANKPOS"):
                    # 解析玩家坦克位置
                    pos = row[15:].strip().split(" ")
                    pos = pos[0].split(",")
                    self.elements.tank_pos = [int(pos[0]) * self.settings.element_size,
                                              int(pos[1]) * self.settings.element_size]
            else:
                # 解析地图元素
                y += 1
                self._parse_element(row, y)

    def _parse_element(self, row, y):
        """解析元素"""
        for x, ele in enumerate(row.strip().split(" ")):
            pos = (x * self.settings.element_size, y * self.settings.element_size)
            # 当前的位置
            if ele == "S":
                continue
            elif ele == "B":
                self.elements.add_brick(Brick(pos, self.res.brick))
            elif ele == "I":
                self.elements.add_brick(Iron(pos, self.res.iron))
