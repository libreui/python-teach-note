class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, game):
        """初始化统计信息"""
        self.score = 0
        self.level = 1
        self.counter = 0

        self.game_active = False
        self.gameover = True

    def clear_score(self):
        self.score = 0
        self.level = 1
        self.counter = 0
