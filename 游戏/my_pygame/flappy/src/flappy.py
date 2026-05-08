import pygame
from config import Config
from pygame.sprite import Group
from background import Background
from bird import Bird
from ground import Ground
from state import State


class Flappy:

    def __init__(self):
        """初始化游戏"""
        self.config = Config() # 游戏配置
        self.state = State(self) # 游戏状态

        pygame.init() # 初始化Pygame
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT)) # 设置游戏窗口大小
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock() # 创建时钟对象

        self.bg_group = Group()

        self.background = Background(self)
        self.ground = Ground(self)

        self.bg_group.add(self.background, self.ground)

        self.bird = Bird(50, 150)


    def start(self):
        """开始游戏"""
        while True:
            self._check_events()
            self._update()
            self._display()

    def _update(self):
        """更新游戏状态"""
        self.bg_group.update()
        # 更新小鸟动画
        self.bird.animation()
        if self.state.game_started:
            self.bird.update()

    def _display(self):
        """显示游戏窗口"""
        self.screen.fill(self.config.BG_COLOR)
        self.background.draw() # 更新背景
        self.ground.draw() # 更新地面
        self.bird.draw(self.screen)
        pygame.display.flip() # 更新显示
        self.clock.tick(self.config.FPS)

    def _check_events(self):
        """检查事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 如果游戏已经开始，小鸟跳跃
                    if self.state.game_started:
                        self.bird.jump()
                    # 如果游戏未结束（游戏还没开始），开始游戏
                    elif not self.state.game_over:
                        self.state.game_started = True


if __name__ == '__main__':
    flappy = Flappy()
    flappy.start()