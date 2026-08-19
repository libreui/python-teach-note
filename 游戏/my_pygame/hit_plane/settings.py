class Settings:
    """游戏设置类"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 512
        self.screen_height = 768
        self.fps = 60
        self.bg_color = (20, 20, 20)
        self.map_speed = 1

        # 飞机设置
        self.scale = 0.7

        # 子弹设置
        self.bullet_color = (255, 165, 0)
        self.bullet_speed = 15.5
        self.bullet_radius = 5

        # 敌人子弹设置
        self.enemy_bullet_color = (255, 255, 255)
        self.enemy_bullet_speed = 5
        self.enemy_bullet_radius = 3

        # 敌人设置
        self.enemy_speed = 1.5

