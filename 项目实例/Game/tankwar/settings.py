class Settings:
    """存储游戏中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 630
        self.screen_height = 630
        self.border_width = 3
        self.bg_color = (0, 0, 0)
        self.fps = 60
        self.animate_speed = 0.2    # 动画速度

        # 坦克速度
        self.tank_speed = 1
        self.enemy_tank_speed = 1
        # 子弹速度
        self.bullet_speed = 2

        # 资源大小
        self.element_size = 24  # 元素大小
        self.brick_size = 24    # 砖块大小
        self.tank_size = 48     # 坦克大小
