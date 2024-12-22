import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """游戏的主框架 & 窗体显示"""
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

        # 创建子弹的编组
        self.bullets = Group()

        # 定义背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘鼠标等事件
            self._check_events()

            # 更新飞船
            self.ship.update()
            # 更新子弹编组
            self._update_bullets()

            # 更新屏幕
            self._update_screen()

    def _update_bullets(self):
        """更新子弹编组"""
        self.bullets.update()

        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """开火"""
        # 只允许3发
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_events(self):
        """处理每次循环中的事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN: # 判断键盘按下事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: # 判断键盘抬起事件
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """处理键盘落下事件"""
        if event.key == pygame.K_q:
            pygame.quit()
            exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  # 发射

    def _check_keyup_events(self, event):
        """处理键盘抬起事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False



    def _update_screen(self):
        """每次循环更新屏幕"""
        # 填充背景色 每次循环都条充一次颜色
        self.screen.fill(self.bg_color)

        # 绘制飞船
        self.ship.blitme()

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 更新屏幕
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    pygame.quit()
