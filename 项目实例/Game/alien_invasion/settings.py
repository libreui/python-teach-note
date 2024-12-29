class Settings:
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed = 2.5

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人的移动速度
        self.alien_speed = 0.03
