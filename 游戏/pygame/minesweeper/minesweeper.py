import random
import sys

import pygame
from pygame.sprite import Sprite


class Minesweeper:
    """扫雷游戏的主类，负责游戏的初始化和运行"""

    def __init__(self):
        """初始化游戏的配置、状态和界面"""
        # 创建游戏配置对象
        self.config = Config()
        # 创建游戏状态对象（管理地雷网格）
        self.state = State(self.config)

        # 初始化pygame
        pygame.init()
        # 设置游戏窗口标题
        pygame.display.set_caption(self.config.caption)
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        # 创建游戏时钟（控制帧率）
        self.clock = pygame.time.Clock()

        # 初始化地雷网格
        self._init_mines()

    def _init_mines(self):
        """初始化地雷网格，创建所有地雷格子对象"""
        for i in range(self.config.grid_size):
            for j in range(self.config.grid_size):
                self.state.mines[i][j] = Mine(self, i, j)

        # 给格子随机分配地雷
        self._assign_mines()

        # 计算所有地雷格子周围地雷数量
        for row in self.state.mines:
            for mine in row:
                if mine is not None:
                    self._calculate_adjacent_mine(mine)

    def _check_events(self):
        """处理游戏事件（键盘、鼠标等）"""
        for event in pygame.event.get():
            # 处理窗口关闭事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 处理鼠标点击事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mines_clicked(event)



    def _check_mines_clicked(self, event):
        """处理鼠标点击地雷格子的事件"""
        # 获取鼠标点击位置
        pos_x, pos_y = pygame.mouse.get_pos()

        row = pos_x // self.config.mines_size
        col = pos_y // self.config.mines_size

        # 当前被点击的格子
        clicked_mine: Mine = self.state.mines[row][col]

        if event.button == 1:
            self._open_mines(clicked_mine)
        elif event.button == 3:
            clicked_mine.set_mark()

    def run(self):
        """游戏主循环"""
        while True:
            # 填充背景色
            self.screen.fill(self.config.bg_color)
            # 控制帧率
            self.clock.tick(self.config.fps)
            # 处理事件
            self._check_events()

            # 绘制所有地雷格子
            self._draw_mines()

            # 更新屏幕显示
            pygame.display.flip()

    def _draw_mines(self):
        """绘制所有地雷格子"""
        for row in self.state.mines:
            for mine in row:
                if mine is not None:
                    mine.draw()

    def _assign_mines(self):
        """给格子随机分配地雷"""
        # 随机打乱所有格子的顺序
        mine_positions = list(range(self.config.grid_size ** 2))
        random.shuffle(mine_positions)

        # 分配地雷
        for i in mine_positions[:self.config.mine_count]:
            row, col = divmod(i, self.config.grid_size)
            self.state.mines[row][col].is_mine = True

    def _calculate_adjacent_mine(self, mine):
        """计算当前被点击格子周围格子的周围地雷数量"""
        # 如果是地雷格子，不计算
        if mine.is_mine:
            return

        # 计算出他周围的8个格子坐标
        adjacent_mines = self._get_adjacent_mines(mine)

        # 计算出当前格子周围地雷数量
        mine.number = sum(1 for row, col in adjacent_mines if self.state.mines[row][col].is_mine)

    def _get_adjacent_mines(self, mine):
        """获取当前格子周围的所有格子"""
        adjacent_mines = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: # 自己
                    continue
                adjacent_mines.append((mine.row + i, mine.col + j))
        # 过滤出有效坐标（在网格范围内）
        valid_adjacent_mines = [mine for mine in adjacent_mines if 0 <= mine[0] < self.config.grid_size and 0 <= mine[1] < self.config.grid_size]
        return valid_adjacent_mines

    def _open_mines(self, mine):
        """
        递归翻开周围的格子
        1. 如果是地雷格子，不递归
        2. 如果当前格子已经翻开，不递归
        3. 打开当前格子
        4. 递归搜索其他格子（只搜索未翻开且非地雷的格子）
        """

        # 如果已经翻开，不递归
        if mine.is_opened:
            return

        # 打开当前格子
        mine.set_opened()

        # 如果是地雷格子，不递归
        # 如果当前格子周围地雷数量不为0，不递归
        if mine.is_mine or mine.number != 0:
            return

        # 当前格子的行列
        row = mine.row
        col = mine.col

        # 递归搜索其他格子
        for dr, dc in self.config.offsets:
            # 检查边界条件，确保不会访问到网格外的格子
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < self.config.grid_size and 0 <= new_col < self.config.grid_size:
                # 获取相邻格子
                adjacent_mine: Mine = self.state.mines[new_row][new_col]
                # 如果相邻格子周围地雷数量为0，递归翻开
                self._open_mines(adjacent_mine)



class Config:
    """游戏配置类，存储游戏的各种参数"""

    def __init__(self):
        """初始化游戏配置参数"""
        # 游戏窗口标题
        self.caption = "Minesweeper"

        # 地雷网格大小（行数和列数）
        self.mines_size = 25
        # 每个格子的像素大小
        self.grid_size = 20
        # 地雷数量
        self.mine_count = self.grid_size ** 2 // 6
        # self.mine_count = 10

        # 游戏窗口宽度（网格大小 × 格子像素大小）
        self.width = self.mines_size * self.grid_size
        # 游戏窗口高度（网格大小 × 格子像素大小）
        self.height = self.mines_size * self.grid_size
        # 游戏帧率
        self.fps = 60
        # 背景颜色（灰色）
        self.bg_color = (192, 192, 192)
        # 八个方向
        self.offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


class State:
    """游戏状态类，存储游戏的当前状态"""

    def __init__(self, config):
        """初始化游戏状态"""
        self.config = config
        # 创建地雷网格（二维列表），初始值为None
        # 用于存储每个格子的地雷对象
        self.mines: list[list[Mine]] = []
        for _ in range(self.config.grid_size):
            # noinspection PyTypeChecker
            self.mines.append([None for _ in range(self.config.grid_size)])


class Mine(Sprite):
    """地雷格子类，继承自Sprite，负责单个地雷格子的显示和交互"""

    def __init__(self, game, row, col):
        """初始化地雷格子"""
        super().__init__()
        # 游戏窗口对象
        self.screen = game.screen
        # 游戏配置对象
        self.config = game.config
        # 行列
        self.row = row
        self.col = col

        # 格子的行坐标（像素）
        self.x = row * self.config.mines_size
        # 格子的列坐标（像素）
        self.y = col * self.config.mines_size
        # 标记状态（是否被右键标记为地雷）
        self.is_marked = False
        # 点击状态（是否被翻开）
        self.is_opened = False
        # 地雷数量
        self.is_mine = False
        # 格子的数字（0-8）
        self.number = 0

        # 加载初始图像（未点击状态）
        self.image = pygame.image.load("./image/9.gif")
        # 获取图像的矩形区域
        self.rect = self.image.get_rect()
        # 设置图像在屏幕上的位置
        self.rect.topleft = (self.x, self.y)

    def _set_image(self):
        """根据当前状态设置图像"""

        # 首先区分格子是否被翻开了
        if self.is_opened:
            if self.is_mine:
                self.image = pygame.image.load("./image/11.gif")
            elif self.number > 0:
                self.image = pygame.image.load(f"./image/{self.number}.gif")
            else:
                self.image = pygame.image.load(f"./image/0.jpg")
        elif self.is_marked:
            self.image = pygame.image.load("./image/10.gif")
        else:
            self.image = pygame.image.load("./image/9.gif")

    def draw(self):
        """在屏幕上绘制地雷格子"""
        self._set_image()
        self.screen.blit(self.image, self.rect)


    def set_mark(self):
        """处理鼠标右键点击事件"""
        if self.is_opened:
            return

        self.is_marked = not self.is_marked


    def set_opened(self):
        """设置格子为已翻开状态"""
        if self.is_marked:
            return

        self.is_opened = True


    def __repr__(self):
        return f"Mine({self.row}, {self.col})"


if __name__ == "__main__":
    """程序入口点"""
    # 创建扫雷游戏对象
    minesweeper = Minesweeper()
    # 运行游戏
    minesweeper.run()