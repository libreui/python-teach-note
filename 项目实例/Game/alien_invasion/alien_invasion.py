import pygame
import sys

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 初始化设置类
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 创建飞船
        self.ship = Ship(self)

        # 定义背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘鼠标等事件
            self._check_events()

            # 更新屏幕
            self._update_screen()


    def _check_events(self):
        """处理每次循环中的事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        """每次循环更新屏幕"""
        # 填充背景色 每次循环都条充一次颜色
        self.screen.fill(self.bg_color)

        # 绘制飞船
        self.ship.blitme()

        # 更新屏幕
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
