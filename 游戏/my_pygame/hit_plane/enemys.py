import math
import pygame
import random
from pygame.sprite import Sprite


class Enemys(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings
        self.color = (255, 255, 255)
        self.hit_color = (255, 0, 0)

        self.w = 50
        self.h = 50
        self.x = random.randint(50, self.screen_rect.width - 50)
        self.y = -50
        self.rect = pygame.Rect(
            self.x, self.y,
            self.w, self.h
        )

        # 初始化角度值
        self.angle = 0
        self.movement = 'straight_down'
        self.speed = self.settings.enemy_speed


        # 计数器,用于闪烁
        self.hit_count = 0
        self.count = 0
        self.direction = 1
        self.is_drop = True

        # 敌人血量
        self.is_hit = False
        self.health = 1

    def set_health(self, health):
        self.health = health

    def set_position(self, i, count, pos_type='random'):
        if pos_type == 'random':
            self.x = random.randint(50, self.screen_rect.width - 50)
        elif pos_type == 'left':
            self.x = self.screen_rect.width // 3
        elif pos_type == 'right':
            self.x = self.screen_rect.width - self.screen_rect.width // 3 - self.w
        elif pos_type == 'center':
            self.x = self.screen_rect.width // 2 - self.w // 2

        # 添加垂直间隙 (例如20像素)，修改间距计算方式
        gap = self.h * 1.5  # 可调整的间隙像素值
        self.y = -(self.h + gap) * (count - i)

    def set_size(self, size_type='small'):
        if size_type == 'small':
            self.w, self.h = 30, 30
        elif size_type == 'medium':
            self.w, self.h = 50, 50
        elif size_type == 'large':
            self.w, self.h = 100, 100

    def set_movement(self, movement_type='straight_down'):
        self.movement = movement_type
        self.speed = self.settings.enemy_speed

    # 被击中
    def hit(self):
        """被击中"""
        self.health -= 1
        self.is_hit = True
        self.hit_count = 0
        if self.health <= 0:
            self.kill()


    def draw_enemy(self):
        self.rect = pygame.Rect(
            self.x, self.y,
            self.w, self.h
        )
        # 如果被击中了闪烁一下
        if self.is_hit:
            pygame.draw.rect(self.screen, self.hit_color, self.rect)
            self.hit_count += 1
            if self.hit_count >= 5:
                self.is_hit = False
                self.hit_count = 0
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edge(self):
        return self.rect.top >= self.screen_rect.bottom


    def update(self):
        """敌机运动 - 基于 movement 属性选择移动方式"""

        if self.movement == "straight_down":
            self._update_line()
        elif self.movement == "zigzag":
            self._update_s()
        elif self.movement == "hover_attack":
            self._update_hover_attack()

    def _update_line(self):
        """直线向下移动"""
        self.y += self.direction * self.speed  # Use configurable speed instead of hardcoded value

    def _update_s(self):
        """Z字形移动 (S曲线)"""
        # 增加角度值（控制摆动频率）
        self.angle += 0.1
        # 计算水平方向位移（正弦函数实现左右摆动）
        dx = 5 * math.sin(self.angle)
        self.x += dx
        # 垂直方向移动使用配置速度
        self.y += self.direction * self.speed

    def _update_hover_attack(self):
        """Hover attack movement: first move to 1/3 screen height,
        then float randomly up & down + horizontal sway"""
        # 1. 基础参数配置
        screen_h = self.screen_rect.height
        target_h = screen_h // 4  # 悬停基准高度：屏幕1/4处
        float_range = 25  # 上下浮动最大幅度
        float_speed = 0.05  # 纵向浮动速度
        sway_speed = 1.2  # 左右横向摆动速度

        # 阶段一：移动到悬停基准高度
        if self.is_drop:
            # 向上/向下靠拢目标高度
            if self.y < target_h:
                self.y += self.settings.enemy_speed
            elif self.y > target_h:
                self.y -= self.settings.enemy_speed
            # 到达目标高度，切换漂浮状态
            if abs(self.y - target_h) < 3:
                self.is_drop = False
                # 重置计数与方向
                self.count = 0
                self.direction = 1

        # 阶段二：抵达高度后，随机上下浮动 + 左右往复摇摆
        else:
            self.count += 1

            # 横向匀速左右摆动
            self.x += self.direction * sway_speed

            # 纵向正弦平滑上下浮动（自然随机漂浮效果）
            offset_y = float_range * math.sin(self.count * float_speed)
            self.y = target_h + offset_y

            # 碰到左右边界反转横向方向
            if self.x <= 0 or self.x >= self.screen_rect.width - self.rect.width:
                self.direction *= -1
