import pygame
from config import Config
from pygame.sprite import Group
from background import Background
from 游戏.my_pygame.flappy.src.ground import Ground


class Flappy:

    def __init__(self):
        """初始化游戏"""
        self.config = Config() # 游戏配置

        pygame.init() # 初始化Pygame
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT)) # 设置游戏窗口大小
        self.clock = pygame.time.Clock() # 创建时钟对象

        self.bg_group = Group()

        self.background = Background(self)
        self.ground = Ground(self)

        self.bg_group.add(self.background, self.ground)


    def start(self):
        """开始游戏"""
        while True:
            self._check_events()
            self._update()
            self._display()

    def _update(self):
        """更新游戏状态"""
        self.bg_group.update()

    def _display(self):
        """显示游戏窗口"""
        self.screen.fill(self.config.BG_COLOR)
        self.background.draw() # 更新背景
        self.ground.draw() # 更新地面
        pygame.display.flip() # 更新显示
        self.clock.tick(self.config.FPS)

    def _check_events(self):
        """检查事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    flappy = Flappy()
    flappy.start()
