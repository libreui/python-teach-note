class Settings:
    """存储游戏《外新人入侵》中所有的设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 0.03
        self.fleet_drop_speed = 20
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # 记分
        self.alien_points = 50
        # 提高外星人点数的等级
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.03

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        # self.ship_speed *= self.speedup_scale
        # self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


