import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


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

        # 保存游戏状态以及统计信息
        self.stats = GameStats(self)

        # 创建飞船
        self.ship = Ship(self)

        # 创建子弹的编组
        self.bullets = Group()

        # 创建一个敌人编组
        self.aliens = Group()
        self._create_fleet()

        # 创建按钮
        self.play_button = Button(self, "Play")

        # 定义背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘鼠标等事件
            self._check_events()

            if self.stats.game_active:
                # 更新飞船
                self.ship.update()
                # 更新子弹编组
                self._update_bullets()

                self._update_aliens()

            # 更新屏幕
            self._update_screen()

    def _update_aliens(self):
        """更新外星人"""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """检查外星人是否触底"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom > screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """
        飞船被攻击以后得方法
        1. 重新创建一批外星人
        2. 让飞船数量-1
        3. 飞船位置居中
        """
        if self.stats.ship_left > 0:
            # 飞船数量减1
            self.stats.ship_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


        # 清空外星人和子弹
        self.bullets.empty()
        self.aliens.empty()

        # 重新创建一批外星人
        self._create_fleet()

        # 让飞船回到正中间
        self.ship.center_ship()



    def _update_bullets(self):
        """更新子弹编组"""
        self.bullets.update()

        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """检测外星人与子弹碰撞"""
        # 碰撞检测，是否碰撞到了敌人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                False, True)
        if not self.aliens:
            # 删除所有子弹
            self.bullets.empty()
            # 创建新的外星人
            self._create_fleet()

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
                sys.exit()
            elif event.type == pygame.KEYDOWN: # 判断键盘按下事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: # 判断键盘抬起事件
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标按下事件
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _start_game(self):
        # self.stats.game_active = True
        pygame.mouse.set_visible(False)
        self.stats.reset_stats()

        # 清空外星人和子弹
        self.aliens.empty()
        self.bullets.empty()

        # 创建新的外星人和飞船
        self._create_fleet()
        self.ship.center_ship()

    def _check_play_button(self, mouse_pos):
        """判断按钮点击是否成功"""
        clicked = self.play_button.rect.collidepoint(mouse_pos)
        if clicked and not self.stats.game_active:
            self._start_game()

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
        elif event.key == pygame.K_p:
            # 游戏开始
            self._start_game()

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

        # 检测外星人碰撞边缘
        self._check_fleet_edges()
        # 绘制敌人
        self.aliens.draw(self.screen)

        # 绘制按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 更新屏幕
        pygame.display.flip()


    def _create_fleet(self):
        """创建并添加敌人"""
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算可以放置外星人的高度
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 绘制一行外星人
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_number * alien_width
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * row_number * alien_height
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有没有外星人碰到边缘"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # 所有外星人改变方向
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        # 首先要改变左右方向
        self.settings.fleet_direction *= -1
        # 下降
        for alien in self.aliens.sprites():
            # alien.rect.y += self.settings.fleet_drop_speed
            alien.down()

    



if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
