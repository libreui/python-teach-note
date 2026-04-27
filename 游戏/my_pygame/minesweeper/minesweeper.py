import random
import sys
from time import sleep

import pygame
from pygame.sprite import Sprite
from typing import Dict


class ResourceManager:
    """资源管理类，负责统一加载和管理游戏资源"""

    def __init__(self):
        """初始化资源管理器"""
        self.mine_images: Dict[str, pygame.Surface] = {}  # 地雷格子资源
        self.head_images: Dict[str, pygame.Surface] = {}  # 头部资源
        self.images_loaded = False

    def load_images(self):
        """加载所有游戏图片资源"""
        if not self.images_loaded:
            try:
                # 加载地雷格子相关图片
                self.mine_images = {
                    "closed": pygame.image.load("./image/grid_unOpen.png"),
                    "mine": pygame.image.load("./image/mine.png"),
                    "mine_click": pygame.image.load("./image/mine_click.png"),
                    "marked": pygame.image.load("./image/grid_flag.png"),
                    "0": pygame.image.load("./image/grid0.png"),
                    "1": pygame.image.load("./image/grid1.png"),
                    "2": pygame.image.load("./image/grid2.png"),
                    "3": pygame.image.load("./image/grid3.png"),
                    "4": pygame.image.load("./image/grid4.png"),
                    "5": pygame.image.load("./image/grid5.png"),
                    "6": pygame.image.load("./image/grid6.png"),
                    "7": pygame.image.load("./image/grid7.png"),
                    "8": pygame.image.load("./image/grid8.png"),
                }

                # 加载头部相关图片
                self.head_images = {
                    "win": pygame.image.load("./image/win.png"),
                    "lose": pygame.image.load("./image/lose.png"),
                    "bg": pygame.image.load("./image/grid_unOpen.png"),
                    "0": pygame.image.load("./image/number0.png"),
                    "1": pygame.image.load("./image/number1.png"),
                    "2": pygame.image.load("./image/number2.png"),
                    "3": pygame.image.load("./image/number3.png"),
                    "4": pygame.image.load("./image/number4.png"),
                    "5": pygame.image.load("./image/number5.png"),
                    "6": pygame.image.load("./image/number6.png"),
                    "7": pygame.image.load("./image/number7.png"),
                    "8": pygame.image.load("./image/number8.png"),
                    "9": pygame.image.load("./image/number9.png"),
                }

                self.images_loaded = True
                print("资源加载成功")
            except pygame.error as e:
                print(f"资源加载失败: {e}")

    def get_mine_images(self) -> Dict[str, pygame.Surface]:
        """获取地雷格子资源"""
        if not self.images_loaded:
            self.load_images()
        return self.mine_images

    def get_head_images(self) -> Dict[str, pygame.Surface]:
        """获取头部资源"""
        if not self.images_loaded:
            self.load_images()
        return self.head_images


class Minesweeper:
    """扫雷游戏的主类，负责游戏的初始化和运行"""

    def __init__(self):
        """初始化游戏的配置、状态和界面"""
        # 创建游戏配置对象
        self.config = Config()
        # 初始化pygame
        pygame.init()
        # 设置游戏窗口标题
        pygame.display.set_caption(self.config.caption)
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        # 创建游戏时钟（控制帧率）
        self.clock = pygame.time.Clock()
        # 需要更新的区域列表
        self.update_rects = []

        # 创建资源管理器
        self.resource_manager = ResourceManager()
        # 加载所有资源
        self.resource_manager.load_images()

        # 创建游戏状态对象（管理地雷网格）
        self.state = State(self.config)

        # 创建头部模块
        self.head = Head(self)

        # 创建精灵编组
        self.mine_sprites = pygame.sprite.Group()

        # 记录状态变化的格子
        self.changed_mines = set()

        # 初始化地雷网格
        self._init_mines()

    def _init_mines(self):
        """初始化地雷网格，创建所有地雷格子对象"""
        for row in range(self.config.grid_size):
            for col in range(self.config.grid_size):
                mine = Mine(self, row, col)
                self.state.mines[row][col] = mine
                # 将所有地雷格子添加到精灵编组
                self.mine_sprites.add(mine)

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
                # 如果游戏结束了，只有点击头部笑脸才能重新开始游戏
                if not self.state.game_over:
                    self._check_mines_clicked(event)

                # 点击笑脸重新开始游戏
                if self.head.on_clicked(event.pos):
                    self.restart_game()

    def _check_game_over(self):
        """检查是否游戏结束"""
        if self.state.game_over:
            self.set_game_over()

    def set_game_over(self):
        """游戏结束后的回调函数"""
        # 打开所有地雷格子
        self._open_all_mines()
        # 通知重绘区域
        self.head.set_changed()
        return

    def restart_game(self):
        """重新开始游戏"""
        # 重置游戏状态
        self.state.reset()
        # 初始化地雷网格
        self._init_mines()
        # 重新绘制所有格子
        self._init_draw()
        # 重置更新区域列表
        self.update_rects.clear()
        # 重置状态变化的格子
        self.changed_mines.clear()

    def _check_mines_clicked(self, event):
        """处理鼠标点击地雷格子的事件"""
        # 获取鼠标点击位置
        pos = event.pos

        if not (0 <= pos[0] < self.config.width and self.config.head_height <= pos[1] < self.config.height):
            return

        col = pos[0] // self.config.mines_size  # x坐标对应的行索引
        row = (pos[1] - self.config.head_height) // self.config.mines_size  # y坐标对应的列索引

        # 当前被点击的格子
        clicked_mine: Mine = self.state.mines[row][col]  # type: ignore

        # 检查是左键还是右键点击
        if event.button == 1:  # 左键
            # 如果点击了地雷，游戏结束
            if clicked_mine.is_mine:
                # 设置因为点了这个格子游戏结束了
                clicked_mine.is_game_over = True
                self.state.set_game_over()
                return
            # 非地雷格子，打开
            self._open_mines(clicked_mine)
        elif event.button == 3:  # 右键
            # 无论是地雷还是非地雷格子，都可以标记
            clicked_mine.set_mark()
            self.head.set_changed()

        # 记录第一次点击格子时间
        if not self.state.game_started:
            self.state.game_started = True
            self.state.start_time = pygame.time.get_ticks() // 1000

    def _init_draw(self):

        # 首次绘制所有格子
        self.screen.fill(self.config.bg_color)
        self.mine_sprites.draw(self.screen)
        pygame.display.flip()

    def _playing_draw(self):
        """绘制游戏进行中的内容"""
        # 绘制头部控件
        self.head.update()

        # 绘制所有地雷格子
        self._draw_mines()

        # 更新屏幕
        if self.update_rects:
            pygame.display.update(self.update_rects)
            self.update_rects.clear()

    def _open_all_mines(self):
        """打开所有地雷格子"""
        for row in self.state.mines:
            for mine in row:
                if mine is not None and not mine.is_opened:
                    mine.is_opened = True
                    mine.set_image()
                    # 绑定到屏幕
                    mine.blit(self.screen)
        # 通知重绘区域
        rect = pygame.Rect(0, self.config.head_height,
                           self.config.width,
                           self.config.height - self.config.head_height)
        self.update_rects.append(rect)

    def _fps_control(self):
        """控制游戏帧率"""
        # 始终保持较高的帧率，确保响应迅速
        self.clock.tick(self.config.fps)

    def run(self):
        """游戏主循环"""
        # 绘制初始内容
        self._init_draw()
        while True:
            # 处理事件
            self._check_events()
            # 检查游戏是否结束
            self._check_game_over()
            # 绘制游戏进行中的内容
            self._playing_draw()
            # 控制帧率
            self._fps_control()

    def _draw_mines(self):
        """绘制所有地雷格子"""
        if self.changed_mines:

            # 收集记录需要重绘的格子
            update_rects = [mine.rect for mine in self.changed_mines]

            # 绘制状态变化的格子
            for mine in self.changed_mines:
                # 绘制一个格子背景，覆盖掉之前的格子
                pygame.draw.rect(self.screen, self.config.bg_color, mine.rect)
                # 绘制当前格子的图片
                self.screen.blit(mine.image, mine.rect)

            # 更新屏幕显示
            # pygame.display.update(update_rects)
            self.update_rects += update_rects

            # 清空状态变化的格子集合
            self.changed_mines.clear()

    def _draw_status(self):
        """绘制游戏状态信息"""
        pass

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
                if i == 0 and j == 0:  # 自己
                    continue
                adjacent_mines.append((mine.row + i, mine.col + j))
        # 过滤出有效坐标（在网格范围内）
        valid_adjacent_mines = [mine for mine in adjacent_mines if
                                0 <= mine[0] < self.config.grid_size and 0 <= mine[1] < self.config.grid_size]
        return valid_adjacent_mines

    def _open_mines(self, mine):
        """
        递归翻开周围的格子
        1. 如果是地雷格子，不递归
        2. 如果当前格子已经翻开，不递归
        3. 打开当前格子
        4. 递归搜索其他格子（只搜索未翻开且非地雷的格子）
        """
        stack = [mine]

        while stack:
            current_mine = stack.pop()

            # 如果已经翻开，不递归
            if current_mine.is_opened:
                continue

            # 打开当前格子
            current_mine.set_opened()

            # 如果是地雷格子，不递归
            # 如果当前格子周围地雷数量不为0，不递归
            if current_mine.is_mine or current_mine.number != 0:
                continue

            # 当前格子的行列
            row = current_mine.row
            col = current_mine.col

            # 递归搜索其他格子
            for dr, dc in self.config.offsets:

                new_row = row + dr
                new_col = col + dc

                # 检查边界条件，确保不会访问到网格外的格子
                if 0 <= new_row < self.config.grid_size and 0 <= new_col < self.config.grid_size:
                    # 获取相邻格子
                    adjacent_mine = self.state.mines[new_row][new_col]
                    # 如果相邻格子周围地雷数量为0，递归翻开
                    if isinstance(adjacent_mine, Mine) and not adjacent_mine.is_opened:
                        stack.append(adjacent_mine)


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
        # 数字图片大小
        self.digit_w = 13
        self.digit_h = 23
        # 地雷数量
        self.mine_count = self.grid_size ** 2 // 6
        # self.mine_count = 10

        # 顶部头部高度
        self.head_height = self.mines_size + 10

        # 游戏窗口宽度（网格大小 × 格子像素大小）
        self.width = self.mines_size * self.grid_size
        # 游戏窗口高度（网格大小 × 格子像素大小）
        self.height = self.mines_size * self.grid_size + self.head_height
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
        # 游戏是否结束，初始值为False，表示游戏进行中
        self.game_over = False
        # 记录被标记的地雷数量
        self._marked_mines = 0
        # 记录当前剩余地雷数量
        self._remaining_mines = 0
        # 倒计时开始时的时间
        self._timer_start_time = 0
        # 游戏开始时间
        self.start_time = 0
        # 游戏是否开始
        self.game_started = False

        # 创建地雷网格（二维列表），初始值为None
        # 用于存储每个格子的地雷对象
        self.mines: list[list[Mine]] = []

        # 初始化地雷网格
        self._init_mines()

    def _init_mines(self):
        """初始化地雷网格"""
        for _ in range(self.config.grid_size):
            # noinspection PyTypeChecker
            self.mines.append([None for _ in range(self.config.grid_size)])

    @property
    def timer_start_time(self):
        """倒计时开始时的时间"""
        return self.config.mine_count * 5

    @property
    def remaining_mines(self):
        """当前剩余地雷数量"""
        return self.config.mine_count - self._marked_mines

    def set_marked_mines(self, marked: bool):
        """增加被标记的地雷数量"""
        if marked:
            self._marked_mines += 1
        else:
            self._marked_mines -= 1

    def minus_remaining_mines(self):
        """减少当前剩余地雷数量"""
        self._remaining_mines -= 1

    def reset(self):
        """重置游戏状态"""

        self.game_over = False
        self._marked_mines = 0
        self._remaining_mines = 0
        self._timer = 0
        self.start_time = 0
        self.game_started = False
        self._init_mines()

    def set_game_over(self):
        """设置游戏结束"""
        self.game_over = True


class Mine(Sprite):
    """地雷格子类，继承自Sprite，负责单个地雷格子的显示和交互"""

    def __init__(self, minesweeper, row, col):
        """初始化地雷格子"""
        super().__init__()
        # 游戏对象
        self.game = minesweeper
        # 游戏状态对象
        self.state = minesweeper.state
        # 游戏窗口对象
        self.screen = minesweeper.screen
        # 游戏配置对象
        self.config = minesweeper.config
        # 行列
        self.row = row
        self.col = col

        # 格子的行坐标（像素）
        self.x = col * self.config.mines_size
        # 格子的列坐标（像素）
        self.y = self._y()
        # 标记状态（是否被右键标记为地雷）
        self.is_marked = False
        # 点击状态（是否被翻开）
        self.is_opened = False
        # 地雷数量
        self.is_mine = False
        # 格子的数字（0-8）
        self.number = 0
        # 是这个格子被点击后游戏使得游戏结束的标志
        self.is_game_over = False

        # 获取地雷格子资源
        self.images = self.game.resource_manager.get_mine_images()
        # 初始图像
        self.image = self.images["closed"]
        # 获取图像的矩形区域
        self.rect = self.image.get_rect()
        # 设置图像在屏幕上的位置
        self.rect.topleft = (self.x, self.y)

    def blit(self, surface):
        """在屏幕上绘制地雷格子"""
        pygame.draw.rect(surface, self.config.bg_color, self.rect)
        surface.blit(self.image, self.rect)

    def set_image(self):
        """根据当前状态设置图像"""

        # 首先区分格子是否被翻开了
        if self.is_opened:
            if self.is_mine:
                if self.is_game_over:
                    self.image = self.images["mine_click"]
                else:
                    self.image = self.images["mine"]
            elif self.number > 0:
                self.image = self.images[str(self.number)]
            else:
                self.image = self.images["0"]
        elif self.is_marked:
            self.image = self.images["marked"]
        else:
            self.image = self.images["closed"]

    # def draw(self, screen):
    #     """在屏幕上绘制地雷格子"""
    #     self._set_image()
    #     screen.blit(self.image, self.rect)

    def _y(self):
        return self.row * self.config.mines_size + self.config.head_height

    def set_mark(self):
        """处理鼠标右键点击事件"""
        if self.is_opened:
            return

        # 切换标记状态
        self.is_marked = not self.is_marked

        # 更新游戏状态
        self.state.set_marked_mines(self.is_marked)

        # 更新图像
        self.set_image()

        # 记录状态变化的格子
        self.game.changed_mines.add(self)

    def set_opened(self):
        """设置格子为已翻开状态"""
        if self.is_marked:
            return

        self.is_opened = True
        # 更新图像
        self.set_image()

        # 记录状态变化的格子
        self.game.changed_mines.add(self)

    def __repr__(self):
        return f"Mine({self.row}, {self.col})"


class Head:
    """头部游戏界面的头部信息"""

    def __init__(self, minesweeper):
        """初始化头部信息"""
        # 游戏对象
        self.game = minesweeper
        # 游戏窗口对象
        self.screen = minesweeper.screen
        # 游戏配置对象
        self.config = minesweeper.config
        # 游戏状态
        self.state = minesweeper.state
        # 设置更新标识
        self.changed = True
        # 头部区域
        self.rect = pygame.Rect(0, 0, self.config.width, self.config.head_height)
        # 笑脸位置
        self.win_rect = pygame.Rect(0, 0, self.config.mines_size, self.config.mines_size)
        self.win_rect.center = self.rect.center

        # 地雷数量区域
        self.mine_digit_rects = []
        for i in range(3):
            rect = pygame.Rect(10 + self.config.digit_w * i,
                               (self.config.head_height - self.config.digit_h) // 2,
                               self.config.mines_size,
                               self.config.mines_size)
            self.mine_digit_rects.append(rect)

        # 倒计时区域
        self.timer_digit_rects = []
        for i in range(3, 0, -1):
            self.timer_rect = pygame.Rect((self.config.width - self.config.digit_w * (i + 1)) - 10,
                                          (self.config.head_height - self.config.digit_h) // 2,
                                          self.config.digit_w,
                                          self.config.digit_h)
            self.timer_digit_rects.append(self.timer_rect)

        # 获取头部资源
        self.images = self.game.resource_manager.get_head_images()
        # 初始图像
        self.image = self.images["win"]

    def _draw_game_status_button(self):
        """绘制游戏状态按钮"""
        # 设置图像
        self.set_image()
        # 绘制游戏状态按钮
        self.screen.blit(self.image, self.win_rect)

    def _draw_mine_count(self):
        """绘制地雷数量区域"""
        # 转换为3位数
        remaining_mines = f"{self.state.remaining_mines:03d}"
        for i, digit in enumerate(remaining_mines):
            if digit in self.images:
                self.screen.blit(self.images[digit], self.mine_digit_rects[i])

    def _draw_timer(self):
        """绘制倒计时区域"""
        elapsed_time = 0
        if self.state.game_started and not self.state.game_over:
            current_time = pygame.time.get_ticks() // 1000
            elapsed_time = self.state.timer_start_time - (current_time - self.state.start_time)
        # 转换为3位数
        timer = f"{elapsed_time:03d}"
        for i, digit in enumerate(timer):
            if digit in self.images:
                self.screen.blit(self.images[digit], self.timer_digit_rects[i])

    def set_image(self):
        """根据当前状态设置图像"""
        if self.state.game_over:
            self.image = self.images["lose"]
        else:
            self.image = self.images["win"]

    def update(self):
        # 绘制头部矩形
        pygame.draw.rect(self.screen, self.config.bg_color, self.rect)
        self._draw_game_status_button()
        self._draw_mine_count()
        self._draw_timer()
        # pygame.display.update(self.rect)
        self.game.update_rects.append(self.rect)
        self.changed = False

    def set_changed(self):
        self.changed = True

    def on_clicked(self, pos):
        """检查是否点击了笑脸"""
        if self.win_rect.collidepoint(pos):
            self.set_changed()
            return True
        return False


if __name__ == "__main__":
    game = Minesweeper()
    game.run()
