class State:
    def __init__(self, flappy):
        """初始化游戏状态"""
        self.flappy = flappy
        self.game_started = False # 游戏是否开始
        self.game_over = False # 游戏是否结束
