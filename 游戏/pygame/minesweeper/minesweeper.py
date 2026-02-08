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
        for i in range(self.config.mines_size):
            for j in range(self.config.mines_size):
                self.state.mines[i][j] = Mine(self, i, j)

    def _check_events(self):
        """处理游戏事件（键盘、鼠标等）"""
        for event in pygame.event.get():
            # 处理窗口关闭事件
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 处理鼠标点击事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mines_clicked(event)

    def _check_mines_clicked(self, event):
        """处理鼠标点击地雷格子的事件"""
        # 获取鼠标点击位置
        pos = pygame.mouse.get_pos()
        # 区分左键还是右键
        if event.button == 1:  # 左键点击
            for row in self.state.mines:
                for mine in row:
                    if mine is not None:
                        mine.on_mouse_left_down(pos)
        elif event.button == 3:  # 右键点击
            for row in self.state.mines:
                for mine in row:
                    if mine is not None:
                        mine.on_mouse_right_down(pos)

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


class Config:
    """游戏配置类，存储游戏的各种参数"""
    
    def __init__(self):
        """初始化游戏配置参数"""
        # 游戏窗口标题
        self.caption = "Minesweeper"

        # 地雷网格大小（行数和列数）
        self.mines_size = 25
        # 每个格子的像素大小
        self.grid_size = 10

        # 游戏窗口宽度（网格大小 × 格子像素大小）
        self.width = self.mines_size * self.grid_size
        # 游戏窗口高度（网格大小 × 格子像素大小）
        self.height = self.mines_size * self.grid_size
        # 游戏帧率
        self.fps = 60
        # 背景颜色（灰色）
        self.bg_color = (192, 192, 192)


class State:
    """游戏状态类，存储游戏的当前状态"""
    
    def __init__(self, config):
        """初始化游戏状态"""
        self.config = config
        # 创建地雷网格（二维列表），初始值为None
        # 用于存储每个格子的地雷对象
        self.mines = [[None for _ in range(self.config.mines_size)] for _ in range(self.config.mines_size)]


class Mine(Sprite):
    """地雷格子类，继承自Sprite，负责单个地雷格子的显示和交互"""
    
    def __init__(self, game, row, col):
        """初始化地雷格子"""
        super().__init__()
        # 游戏窗口对象
        self.screen = game.screen
        # 游戏配置对象
        self.config = game.config
        # 格子的行坐标（像素）
        self.x = row * self.config.mines_size
        # 格子的列坐标（像素）
        self.y = col * self.config.mines_size
        # 标记状态（是否被右键标记为地雷）
        self.mark = False
        # 点击状态（是否被左键点击）
        self.is_clicked = False

        # 加载初始图像（未点击状态）
        self.image = pygame.image.load("./image/9.gif")
        # 获取图像的矩形区域
        self.rect = self.image.get_rect()
        # 设置图像在屏幕上的位置
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        """在屏幕上绘制地雷格子"""
        self.screen.blit(self.image, self.rect)

    def on_mouse_right_down(self, pos):
        """处理鼠标右键点击事件"""
        # 检查鼠标是否点击在当前格子上
        if self.rect.collidepoint(pos):
            # 如果格子已经被点击，则不处理
            if self.is_clicked:
                return
            # 切换标记状态（标记/取消标记）
            self.mark = not self.mark
            # 根据标记状态更新图像
            if self.mark:
                # 标记为地雷的图像
                self.image = pygame.image.load("./image/10.gif")
            else:
                # 未标记的图像
                self.image = pygame.image.load("./image/9.gif")

    def on_mouse_left_down(self, pos):
        """处理鼠标左键点击事件"""
        # 检查鼠标是否点击在当前格子上，且格子未被标记
        if self.rect.collidepoint(pos) and self.mark is not True:
            # 更新为已点击的图像（数字0）
            self.image = pygame.image.load("./image/0.jpg")
            # 设置为已点击状态
            self.is_clicked = True


if __name__ == "__main__":
    """程序入口点"""
    # 创建扫雷游戏对象
    minesweeper = Minesweeper()
    # 运行游戏
    minesweeper.run()